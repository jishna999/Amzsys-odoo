from odoo import models


class SaleOrderSerial(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrderSerial, self).action_confirm()

        # for picking in self.picking_ids:
        #     picking.stock_reference = self.stock_reference

        sale_order_lines = self.mapped('order_line')

        # mapped One2Many field from sale.order to sale.order.line

        # In the SaleOrder model, the order_line field allows you to access all the lines(products, quantities,
        # etc.) associated with a particular sales order. In the SaleOrderLine model, the order_id field tells you
        # which sales order a particular line belongs to.

        for line in sale_order_lines:
            stock_moves = self.env['stock.move'].search([('sale_line_id', '=', line.id)])

            # sale_line_id is the Many2one field from stock.move to sale.order.line in sale_stock module by search
            # from inherited stock.move modules Here, it's looking for stock.move records where the sale_line_id
            # field matches the ID of the sale.order.line record referred to by line. ' line.id: This refers to the
            # ID of the sale.order.line record currently being processed.

            for move in stock_moves:
                move.lot_ids = line.serial_no_id

        for move in self.mapped(
                'order_line.move_ids'):  # move_ids is One2many field from sale.order.line to stock.move in
            # sale_stock module

            for move_line in move.move_line_ids:  # move_line_ids one2many relation from stock.move to
                # stock.move.lines
                move_line.lot_id = move.lot_ids

        return res

    def _create_invoices(self, grouped=False, final=False):
        result = super(SaleOrderSerial, self)._create_invoices(self)

        sale_order_lines = self.mapped('order_line')

        for line in sale_order_lines:
            account_moves = self.env['account.move.line'].search([('sale_line_ids', '=', line.id)])

            # Many2many field from account.move.line to sale.order.line and there is
            # also field invoice_lines Many2Many relation from sale.order.line to account.move.line

            for account_move in account_moves:
                account_move.serial_no_id = line.serial_no_id

        return result