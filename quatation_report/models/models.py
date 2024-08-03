# from odoo import models, fields
#
#
# class SaleOrder(models.Model):
#     _inherit = 'sale.order'
#
#     def action_preview_sale_order(self):
#         self.ensure_one()
#
#         return {
#             'type': 'ir.actions.act_url',
#             'target': 'self',
#             'url': self.get_portal_url(),
#         }
