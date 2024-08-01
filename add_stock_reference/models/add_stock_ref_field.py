from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    stock_reference = fields.Char(string='Stock Reference')

    def _action_confirm(self):
        result = super(SaleOrder, self)._action_confirm()
        for picking in self.picking_ids:
            picking.stock_reference = self.stock_reference
            for move in picking.move_lines:
                move.stock_reference = self.stock_reference
        return result


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    stock_reference = fields.Char(string='Stock Reference')


class StockMove(models.Model):
    _inherit = 'stock.move'

    stock_reference = fields.Char(string='Stock Reference')
