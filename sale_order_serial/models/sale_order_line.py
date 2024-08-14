from odoo import models, fields, api


class SaleOrderSerialLine(models.Model):
    _inherit = 'sale.order.line'

    serial_no_id = fields.Many2one(comodel_name='stock.lot', string="Serial Number",
                                   domain="[('product_id', '=', product_id)]")
