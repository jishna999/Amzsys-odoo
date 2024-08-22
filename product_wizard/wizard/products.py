from odoo import models, fields, api

class SaleOrderAddProductWizard(models.TransientModel):
    _name = 'sale.order.add.product.wizard'
    _description = 'Wizard to Add Products to Sale Order'

    order_id = fields.Many2one('sale.order', string='Sale Order',require=True)
    product_ids = fields.Many2many('product.product', string='Products')

    def action_add_products(self):
        sale_order = self.order_id
        for product in self.product_ids:
            self.env['sale.order.line'].create({
                'order_id': sale_order.id,
                'product_id': product.id,
                'product_uom_qty': 1,
            })
        return {'type': 'ir.actions.act_window_close'}
