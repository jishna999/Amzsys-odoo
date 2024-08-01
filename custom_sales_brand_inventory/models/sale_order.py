from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    order_line = fields.One2many('sale.order.line', 'order_id', string='Order Lines')

    def _action_confirm(self):
        result = super(SaleOrder,self)._action_confirm()

        for order in self:
            for line in order.order_line:
                for move in line.move_ids:
                    move.brand_name = line.product_brand
        return result


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_brand = fields.Char(string="product Brand", related='product_id.product_brand_id.brand_name')


