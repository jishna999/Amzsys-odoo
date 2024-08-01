# -*- coding: utf-8 -*-

from odoo import models, fields


class StockMove(models.Model):
    _inherit = 'stock.move'

    brand_name = fields.Char(string="Product Brand")
