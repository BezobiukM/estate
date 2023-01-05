from odoo import fields, models, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "estate property offer model"

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

    create_date = fields.Date(string='Creation Date',
        default=(lambda self: (fields.Datetime.now())))
    
    _sql_constraints = [
        ('positive_offer_price', 'CHECK (price>0)', 'The price in offer should be grater then 0.')
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
        
        
