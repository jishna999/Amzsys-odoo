from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    stock_reference = fields.Char(string='Stock Reference')


class StockMove(models.Model):
    _inherit = 'stock.move'

    product_brand_id = fields.Many2one('product.brand', string='Product Brand')
    lots_id = fields.Many2one('stock.lot', string='Serial Number')
    serial_ids = fields.Many2many(comodel_name='stock.lot', string="Serial Numbers")


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    lots_id = fields.Many2one('stock.lot', string='Serial Number')
    serial_ids = fields.Many2many(comodel_name='stock.lot', string="Serial Numbers")
