# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
   _inherit = 'sale.order'


   def action_purchase_order(self):

        return {
            'type': 'ir.actions.act_window',
            'name':'Purchase order',
            'view_mode': 'form',
            'res_model':'custom.purchase.order',
            'default_context_sale_order_id':self.id

        }
