from odoo import models, fields


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    product_brand = fields.Many2one('product.brand', string='Product Brand')
    serial_no_id = fields.Many2one(comodel_name='stock.lot', string='Serial number')
    serial_ids = fields.Many2many(comodel_name='stock.lot', string='Serial numbers')
