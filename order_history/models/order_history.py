from odoo import models, fields, api

class OrderHistory(models.Model):
    _name = 'order.history'
    _description = 'Order History'

    order_id = fields.Many2one(
        comodel_name='sale.order',
        string="Order"
    )
    order_line_id = fields.Many2one(
        comodel_name='sale.order.line',
        string='Order line'
    )
    order_history_selected = fields.Boolean(
        string='Re-Order'
    )
    name = fields.Char(
        string='Sale Order'
    )
    date_order = fields.Datetime(
        string='Order Date'
    )
    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Product'
    )
    price = fields.Float(
        string='Price'
    )
    qty_unit = fields.Float(
        string='Quantity Unit'
    )
    discount = fields.Float(
        string='Discount'
    )
    amount_total = fields.Float(
        string='Sub Total'
    )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('sale', 'Sale'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Order Status')


    def action_reorder(self):
        return self.order_id.action_reorder()