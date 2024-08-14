from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    suggested_product_ids = fields.One2many(
        comodel_name='suggested.product',
        inverse_name='order_id',
        string="Suggested Products"
    )

    # def action_confirm(self):
    #     res = super(SaleOrder, self).action_confirm()
    #
    #     suggested_product_lines = self.mapped('suggested_product_ids')  # one2many from sale order to sale.order.line
    #
    #     for suggested in suggested_product_lines:
    #
    #         suggested.product_id = self.product_id
    #
    #         # stock_moves = self.env['stock.move'].search([('sale_line_id', '=', line.id)])
    #         # for move in stock_moves:
    #         #     move.lots_id = line.serial_no_id
    #         #     move.serial_ids = line.serial_ids
    #         #     move.product_brand_id = line.product_brand_id
    #
    #         stock_moves.picking_ids.write({'product_brand_id': stock_moves.order_line.mapped('product_brand_id').id})
    #
    #     for move in self.mapped('order_line.move_ids'):
    #         for move_line in move.move_line_ids:
    #             move_line.lots_id = move.lots_id
    #             move_line.serial_ids = move.serial_ids
    #
    #     return res

    def _create_invoices(self, grouped=False, final=False):

        invoice_vals_list = super(SaleOrder, self)._create_invoices(grouped, final)

        for order in self:

            invoices = self.env['account.move'].search([('invoice_origin', '=', order.name)])

            for invoice in invoices:

                suggested_product_vals = []
                for suggested_product in order.suggested_product_ids:
                    suggested_product_vals.append((
                        0, 0, {
                            'product_id': suggested_product.product_id.id,
                            'product_uom_qty': suggested_product.product_uom_qty,
                            'sale_price': suggested_product.sale_price,
                        }
                    ))

                if suggested_product_vals:
                    invoice.write({'suggested_product_ids': suggested_product_vals})

        return invoice_vals_list
