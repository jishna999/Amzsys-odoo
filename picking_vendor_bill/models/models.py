# -*- coding: utf-8 -*-
from addons.test_base_import.models.test_base_import import model
from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    bill_id =fields.Many2one(comodel_name='account.move')


class PurchaseOrder(models.Model):
    _inherit = 'purchase_order'

    bill_ids =fields.One2many('account.move','purchase_id',string='Bills')
