from odoo import fields, models
from dateutil.relativedelta import relativedelta

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "estate property type model"

    name = fields.Char('Property Type name', required=True)
    description = fields.Char('Property Type descr')
    postcode = fields.Char('Postcode')
    date_availability = fields.Date('Availabile From', 
        default=(lambda self: (fields.Datetime.now()+relativedelta(months=3)) ), copy=False)
    expected_price = fields.Float('Expected Price', required=True)
    selling_price = fields.Float('Selling Price', 
        readonly=True, copy=False)
    salesman = fields.Char('Salesman', required=True)
    buyer = fields.Char('Buyer', required=True)

