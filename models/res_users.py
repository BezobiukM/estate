from odoo import fields, models


class Users(models.Model):
    _inherit = 'res.users'

    property_ids = fields.One2many('estate.property', 'salesman')

    def get_properties_user(self):
        return {
            'name': ('Property'),
            'type': 'ir.actions.act_window',
            'res_model': 'estate.property',
            'view_mode': 'tree,form',
            'domain': [('partner_id', '=', self.env.context.get('active_id'))]
        }