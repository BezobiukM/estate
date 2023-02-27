# -*- coding: utf-8 -*-

import logging

from dateutil.relativedelta import relativedelta

from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_is_zero, float_compare

_logger = logging.getLogger(__name__)


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"
    _order = 'id desc'

    _sql_constraints = [
        ('check_expected_price', 'CHECK (expected_price>0)',
         'The expected price must be grater than 0.'),
        ('check_selling_price', 'CHECK (selling_price>=0)',
         'The selling price must be positive.'),
    ]

    name = fields.Char('Title', required=True)
    tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    property_type_id = fields.Many2one(
        'estate.property.type', string='Property Type')
    expected_price = fields.Float('Expected Price', required=True)
    postcode = fields.Char('Postcode')
    best_price = fields.Float('Best Offer Price', compute='_compute_best_price',
                              readonly=True, copy=False, store=True, help="Best offer received")
    date_availability = fields.Date('Available From',
                                    default=(lambda self: (fields.Datetime.now()+relativedelta(months=3))), copy=False)
    selling_price = fields.Float('Selling Price', readonly=True, copy=False)

    active = fields.Boolean('Active', default=True)
    state = fields.Selection(string="Status",
        selection=[
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('cancelled', 'Cancelled')],
        required=True, copy=False, default='new',
        compute='_compute_state', store=True
    )

    bedrooms = fields.Integer('Bedrooms', default=2)
    living_area = fields.Integer('Living Area (sqm)')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area (sqm)')
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'),
                   ('east', 'East'), ('west', 'West')
                   ])

    salesman = fields.Many2one(
        'res.users', string='Salesman', required=True, default=lambda self: self.env.user,
        domain=[('company_id', 'in', lambda self: self.env.user.company_ids)])
    buyer = fields.Many2one('res.partner', string='Buyer')
    description = fields.Text('Description')
    company_id = fields.Many2one('res.company', required=True, 
                                 default=lambda self: self.env.user.company_id)

    offer_ids = fields.One2many(
        'estate.property.offer', 'property_id', string='Offers')

    total_area = fields.Integer(
        compute="_compute_total_area", string='Total Area (sqm)', store=True,
        help="Total area computed by summing the living area and the garden area",)

    # Compute methods
    @api.depends("offer_ids")
    def _compute_best_price(self):
        for record in self:
            offer_prices = record.offer_ids.mapped("price")
            if offer_prices:
                record.best_price = max(offer_prices)
            # else:
            #     record.best_price = 0.0

    @api.depends("offer_ids", "offer_ids.offer_status")
    def _compute_state(self):
        for record in self:
            if record.state in ('sold', 'cancelled'):
                return
            if any(offer.offer_status == 'accepted' for offer in record.offer_ids):
                record.state = 'offer_accepted'
            elif len(record.offer_ids) >= 1:
                record.state = 'offer_received'
            else:
                record.state = 'new'

    @api.depends("offer_ids")
    def _compute_selling_price(self):
        for record in self:
            if record.offer_ids.offer_status == "accepted":
                record.selling_price = record.offer_ids.price
    
    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        if domain is None:
            domain = []

        if (self.env.user.has_group('estate.estate_group_user')
                and not self.env.user.has_group('estate.estate_group_manager')):
            domain += [
                '|', ('company_id', '=', False), ('company_id', 'in', self.env.user.company_ids.ids),
                '|', ('salesman', '=', False), ('salesman', '=', self.env.user.id)]
        elif (self.env.user.has_group('estate.estate_group_user')
              and self.env.user.has_group('estate.estate_group_manager')):
            domain += [
                '|', ('company_id', '=', False), ('company_id', 'in', self.env.user.company_ids.ids)]

        return super(EstateProperty, self).search_read(
            domain=domain, fields=fields, offset=offset, limit=limit, order=order
        )

    # Constraints and onchanges
    @api.constrains("selling_price")
    def _check_selling_price_value(self):
        for record in self:
            if float_is_zero(record.selling_price, precision_digits=2):
                raise ValidationError("The selling price is not set. Fill in the required fields.")
            if float_compare(record.expected_price*0.9, record.selling_price, precision_digits=2) > 0:
                raise ValidationError(
                    'The offer price is less than 90 percent of the expected price!\n '
                    'You must reduce the expected price if you want to accept this offer.')

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = None
            self.garden_orientation = None
  
    # CRUD methods
    @api.ondelete(at_uninstall=False)
    def _unlink_if_new_or_cancelled(self):
        for record in self:
            if record.state not in ('new', 'cancelled'):
                # _logger.error(
                #     "**************property_record**************************************\n")
                # _logger.error(record.state)
                # _logger.error(record.state != ('new', 'cancelled'))
                # _logger.error(
                #    "**************property_record*end*************************************")
                raise UserError(
                    f"You can delete only the estate property with state New or Cancelled!\n"
                    f" Property [{record.name}] has state: {record.state}")

    #actions
    def action_property_sold(self):
        for record in self:
            if record.state == 'cancelled':
                raise UserError(
                    'Status Cancelled for property can not be changed to Sold!')
            if float_is_zero(record.selling_price, precision_digits=2):
                raise ValidationError("The selling price is not set. You must accept an offer.") 
            record.state = 'sold'
        return True

    def action_property_cancelled(self):
        for record in self:
            if record.state == 'sold':
                raise UserError(
                    'Status Sold for property can not be changed to Cancelled!')
            record.state = 'cancelled'
        return True
