# -*- coding: utf-8 -*-
from setuptools._entry_points import _

from odoo import models, fields, api
from odoo.tools.populate import compute


class PurchaseOrderLines(models.Model):
    _inherit = 'purchase.order.line'

    sale_order_id = fields.Many2one(comodel_name='sale.order.line')
    vendors_id = fields.Many2one(comodel_name='res.partner')
    schedule_date = fields.Datetime(related='sale_order_id.date_order')

    def action_purchase_order(self):
        po = self.sale_order_id

        po_value = {
            'product_id': po.product_id.id,
            'name': po.description,
            'product_qty': po.order_quantity,
            'date_planned': self.schedule_date,
            'unit_price': po.unit_price,
            'price_total': po.total
        }
        purchase_order = super(PurchaseOrderLines).create(po_value)
        return purchase_order

class SalePurchaseOrderLines(models.Model):
    _name = 'sale.puchase.order.lines'

    purchase_line_ids = fields.One2many(comodel_name='purchase.order', inverse_name='sale_order_id')
    product_id = fields.Many2one(comodel_name='product.product', string='Products')
    description = fields.Float(string='description', related='purchase_line_ids.name')
    order_quantity = fields.Float(string='Order Quantity', related='purchase_line_ids.product_uom_qty')
    unit_price = fields.Float(string='Unit price', related='purchase_line_ids.price_unit')
    total = fields.Float(string='Total', compute='_compute_total')

    @api.depends(unit_price, order_quantity)
    def _compute_total(self):
        self.total = self.unit_price * self.order_quantity
        return self.total
