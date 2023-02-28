from odoo import fields, models, api


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Property Types"
    _order = 'sequence, name'

    name = fields.Char('Property Type', required=True)

    salesman = fields.Many2one('res.users', string='Salesman', required=True, default=lambda self: self.env.user)
    buyer = fields.Many2one('res.partner', string='Buyer', required=True)
    description = fields.Text('Description')

    property_ids = fields.One2many('estate.property', 'property_type_id', string='Property')

    sequence = fields.Integer('Sequence', default=1)
    offer_ids = fields.One2many('estate.property.offer', 'property_type_id')
    offer_count = fields.Integer(compute='_compute_offer_count', store=True)

    _sql_constraints = [
        ('estate_property_type_unique', 'UNIQUE (name)', 'The property type name should be unique.')
    ]

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)
