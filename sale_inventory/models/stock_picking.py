# -*- coding: utf-8 -*-

from odoo import models, fields


class StockPicking(models.Model):
    _rec_name = 'stock_reference'
    _inherit = 'stock.picking'
    _description = 'Stock picking details'

    stock_reference = fields.Char(string='Stock reference')

