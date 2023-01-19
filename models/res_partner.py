from odoo import models, fields


class Partner(models.Model):
    _inherit = 'res.partner'

    property_ids = fields.One2many('estate.property', 'buyer')

    def get_properties_partner(self):
        return {
            'name': ('Property'),
            'type': 'ir.actions.act_window',
            'res_model': 'estate.property',
            'view_mode': 'tree,form',
            'domain': [('partner_id', '=', self.env.context.get('active_id'))]
        }