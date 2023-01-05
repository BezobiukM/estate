from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "estate property type model"
    _order = 'sequence, name'

    name = fields.Char('Property Type', required=True)
    
    salesman = fields.Many2one('res.users', string='Salesman', required=True, default=lambda self: self.env.user)
    buyer = fields.Many2one('res.partner', string='Buyer', required=True)
    description = fields.Text('Description')

    property_ids = fields.One2many('estate.property', 'property_type_id', string='Property')

    sequence = fields.Integer('Sequence', default=1)

    _sql_constraints = [
        ('estate_property_type_unique', 'UNIQUE (name)', 'The property type name should be unique.')
    ]  
