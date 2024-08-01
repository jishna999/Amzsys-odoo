# -*- coding: utf-8 -*-

from odoo import models, fields


class StockPicking(models.Model):
    _inherit = 'stock.picking'
    _rec_name = 'stock_reference'

    stock_reference = fields.Char(string='Stock Reference')
