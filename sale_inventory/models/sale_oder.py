# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    stock_reference = fields.Char(string='Stock Reference', required=True)

    def _action_confirm(self):
        result = super(SaleOrder, self)._action_confirm()
        for pickings in self.picking_ids:
            pickings.stock_reference = self.stock_reference
        return result
