from odoo import fields, models,api

class OrderHistory(models.Model):
    _name = 'order.history'
    _description = 'Order History'

    order_id = fields.Many2one(
        comodel_name='sale.order',
        string='Sale Order',
        required=True,
        ondelete='cascade'
    )
    order_line_id = fields.Many2one(
        comodel_name='sale.order.line',
        string='Order Line',
        required=True
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
        string='Sub Total',
        compute='_compute_amount_total',
        store=True
    )
    state = fields.Selection(
        string='Order Status',
        selection='_get_allowed_states',

    )

    @api.depends('price', 'qty_unit', 'discount')
    def _compute_amount_total(self):
        for record in self:
            record.amount_total = (record.price * record.qty_unit) - record.discount

    def _get_allowed_states(self):
        order_stages = self.env['res.config.settings'].sudo().get_values().get('order_stages', 'all')

        allowed_states = [
            ('draft', 'Quotation'),
            ('sent', 'Quotation Sent'),
            ('sale', 'Sale Order'),
            ('done', 'Done'),
            ('cancel', 'Cancelled'),
        ]

        if order_stages == 'all':
            return allowed_states


        filtered_state = [(stage, label) for stage, label in allowed_states if stage == order_stages]
        return filtered_state if filtered_state else allowed_states

    def action_reorder(self):
        if self.order_id:
            self.write({'order_history_selected': True})
            return self.order_id.action_reorder()