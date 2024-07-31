from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    order_line = fields.One2many('sale.order.line', 'order_id', string='Order Lines')


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_brand = fields.Char(string="product Brand", related='product_id.product_brand_id.brand_name')


