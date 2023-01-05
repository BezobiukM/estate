from odoo import fields, models

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "estate property tags model"

    name = fields.Char('Property Tags', required=True)

    _sql_constraints = [
        ('estate_property_tag_unique', 'UNIQUE(name)', 'The tag name should be unique.')
    ]   