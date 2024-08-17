from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    order_history_ids = fields.One2many(
        comodel_name='order.history',
        inverse_name='order_id',
        string='Order History'
    )



    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:

            sale_orders = self.env['sale.order'].search([('partner_id', '=', self.partner_id.id)])
            histories = []
            for order in sale_orders:
                for line in order.order_line:
                    histories.append((0, 0, {
                        'order_id': order.id,
                        'order_line_id': line.id,
                        'name': order.name,
                        'date_order': order.date_order,
                        'product_id': line.product_id.id,
                        'price': line.price_unit,
                        'qty_unit': line.product_uom_qty,
                        'discount': line.discount,
                        'amount_total': line.price_total,
                        'state': order.state,
                    }))
            self.order_history_ids = histories



    def action_reorder(self):


        order = self.env['sale.order'].create({
            'partner_id': self.partner_id.id,
        })

        order_lines = []
        for history in self.order_history_ids.filtered('order_history_selected'):
            order_lines.append((0, 0, {
                'product_id': history.product_id.id,
                'product_uom_qty': history.qty_unit,
                'price_unit': history.price,
                'discount': history.discount,
            }))

        order.write({
            'order_line': order_lines,
            'state': 'sent',
        })

        return {
            'type': 'ir.actions.act_window',
            'name': 'Sale Order',
            'view_mode': 'form',
            'res_model': 'sale.order',
            'res_id': order.id,
            'target': 'current',
        }
