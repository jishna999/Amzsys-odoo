# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class order_history(models.Model):
#     _name = 'order_history.order_history'
#     _description = 'order_history.order_history'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

