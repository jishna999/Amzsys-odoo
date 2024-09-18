from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    purchase_order_count = fields.Integer(
        compute='_compute_purchase_order_count',
        readonly=True
    )
    purchase_ids = fields.One2many('purchase.order', 'sale_order_id', string='Purchase Orders')

    @api.depends('purchase_ids')
    def _compute_purchase_order_count(self):
        for order in self:
            order.purchase_order_count = len(order.purchase_ids)

    def action_view_purchase_orders(self):

        action = super(SaleOrder, self).action_view_purchase_orders()
        action['domain'] = [('sale_order_id', '=', self.id)]
        action['context'] = dict(self.env.context, create=False)

        if len(self.purchase_ids) == 1:
            action['view_mode'] = 'form'
            action['res_id'] = self.purchase_ids.id

        return action




