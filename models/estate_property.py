from dateutil.relativedelta import relativedelta
from odoo import api, fields, models
from odoo.exceptions import UserError


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate property model"

    name = fields.Char('Title', required=True)
    tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    expected_price = fields.Float('Expected Price', required=True)
    postcode = fields.Char('Postcode')
    best_price = fields.Float('Best Offer', compute='_compute_best_price', 
        readonly=True, copy=False, store=True)
    date_availability = fields.Date('Available From',
        default=(lambda self: (fields.Datetime.now()+relativedelta(months=3)) ), copy=False)
    selling_price = fields.Float('Selling Price', readonly=True, copy=False)
    
    active = fields.Boolean('Active', default=True)
    state = fields.Selection(
        selection=[
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('canceled', 'Canceled')],
         required=True, copy=False, default='new'
    )
    bedrooms = fields.Integer('Bedrooms', default=2)
    living_area = fields.Integer('Living Area (sqm)', required=True)
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area (sqm)')
    garden_orientation = fields.Selection(
        string = 'Garden Orientation',
        selection = [('north', 'North'), ('South', 'South'),
        ('east', 'East'), ('west', 'West')
        ])

    salesman = fields.Many2one('res.users', string='Salesman', required=True, default=lambda self: self.env.user)
    buyer = fields.Many2one('res.partner', string='Buyer')
    description = fields.Text('Description')

    offer_ids = fields.One2many('estate.property.offer', 'property_id', string='Offer')

    total_area = fields.Integer(compute="_compute_total_area", string='Total Area (sqm)', store=True)
    
    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids")
    def _compute_best_price(self):
        for record in self:
            offer_prices = record.offer_ids.mapped("price")
            if offer_prices:
                record.best_price = max(offer_prices)

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = None
            self.garden_orientation = None

    
    
    def action_property_sold(self):
        for record in self:
            if self.state == 'canceled':
                raise UserError('Cancelled property can not be sold!')
            record.state = 'sold'
        return True

    
    def action_property_canceled(self):
        for record in self:
            if self.state == 'sold':
                raise UserError('Sold property can not be canceled!')
            record.state = 'canceled'

        return True

    @api.depends("offer_ids")
    def _compute_selling_price(self):
        for record in self:
            if record.offer_ids.offer_status == "accepted":
                record.selling_price = record.offer_ids.price

    