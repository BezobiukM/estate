from odoo import fields, models
from dateutil.relativedelta import relativedelta

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "estate property type model"

    name = fields.Char('Property Type', required=True)
    
    salesman = fields.Many2one('res.users', string='Salesman', required=True, default=lambda self: self.env.user)
    buyer = fields.Many2one('res.partner', string='Buyer', required=True)
    description = fields.Text('Description')

    _sql_constraints = [
        ('estate_property_type_unique', 'UNIQUE (name)', 'The property type name should be unique.')
    ]  
