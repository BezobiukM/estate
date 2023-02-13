from odoo import fields, models

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Real Estate Property Tags"
    _order = 'name'

    name = fields.Char('Property Tags', required=True)
    color = fields.Integer()

    _sql_constraints = [
        ('estate_property_tag_unique', 'UNIQUE(name)', 'The tag name should be unique.')
    ]   