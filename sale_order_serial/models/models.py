# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class sale_order_serial(models.Model):
#     _name = 'sale_order_serial.sale_order_serial'
#     _description = 'sale_order_serial.sale_order_serial'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

