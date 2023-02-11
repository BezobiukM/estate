import logging

from odoo import fields, models, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError


_logger = logging.getLogger(__name__)


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "estate property offer model"
    _order = 'price desc'

    name = fields.Char()
    price = fields.Float('Price')
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    validity = fields.Integer('Validity (days)', default=7)
    deadline = fields.Date('Deadline',
        compute='_compute_deadline',inverse='_inverse_deadline')
    offer_status = fields.Selection(
        selection=[
            ('accepted', 'Accepted'),
            ('refused', 'Refused')],
        copy=False, default=None)
    property_id = fields.Many2one('estate.property', required=True)
    property_type_id = fields.Many2one(related='property_id.property_type_id', store=True)  

    create_date = fields.Date(string='Creation Date',
        default=(lambda self: (fields.Datetime.now())))
    
    _sql_constraints = [
        ('positive_offer_price', 'CHECK (price>0)', 'The price in offer should be grater than 0.')
    ]

    @api.depends('validity')
    def _compute_deadline(self):
        for record in self:
            record.deadline = record.create_date +relativedelta(days=record.validity)
    
    def _inverse_deadline(self):
        for record in self:
            record.validity = relativedelta(record.deadline, record.create_date).days

    def action_offer_accepted(self):
        for record in self:
            is_accepted = record.property_id.offer_ids.filtered(lambda r:r.offer_status=='accepted')
            if is_accepted and record not in is_accepted:
                raise UserError('Only one offer can be accepted!')
            record.offer_status = 'accepted'
            record.property_id.selling_price = record.price
            record.property_id.buyer = record.partner_id
    
    def action_offer_refused(self):
        for record in self:
            if record.offer_status == 'accepted':
                record.property_id.selling_price = 0
                record.property_id.buyer = None
            record.offer_status = 'refused'
    
    @api.model
    def create(self, vals):
        property_record = self.env['estate.property'].browse(vals['property_id']).exists()
        _logger.error("!!!!!!!!!!!!********create*start*********************************************")
        _logger.error(vals)
        _logger.error("!!!!!!!!!!!!!!!!!****create*end*************************************************")
        if property_record and property_record.best_price > vals['price']:
            raise UserError('The offer price must be higher than {0}!'.format(property_record.best_price))
        return super(EstatePropertyOffer, self).create(vals)

    
    @api.model
    def write(self, vals):
        property_record = self.env['estate.property']
        _logger.error("**************write*start*vals**************************************")
        _logger.error(vals)
        _logger.error("**************write*end*vals**************************************")
        if property_record and property_record.best_price > vals['price']:
            raise UserError('The offer price must be higher than {0}!!'.format(property_record.best_price))
        return super(EstatePropertyOffer, self).write(vals)