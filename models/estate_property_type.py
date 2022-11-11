from odoo import fields, models
from dateutil.relativedelta import relativedelta

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "estate property type model"

    name = fields.Char('Property Type', required=True)
    expected_price = fields.Float('Expected Price', required=True)
    postcode = fields.Char('Postcode')
    selling_price = fields.Float('Selling Price', 
        readonly=True, copy=False)
    date_availability = fields.Date('Availabile From', 
        default=(lambda self: (fields.Datetime.now()+relativedelta(months=3)) ), copy=False)
    
    salesman = fields.Many2one('res.users', string='Salesman', required=True, default=lambda self: self.env.user)
    buyer = fields.Many2one('res.partner', string='Buyer', required=True)
    description = fields.Text('Description')

