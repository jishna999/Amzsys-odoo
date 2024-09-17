# -*- coding: utf-8 -*-
# from odoo import http


# class SaleOrderToPurchaseOrder(http.Controller):
#     @http.route('/sale_order_to_purchase_order/sale_order_to_purchase_order', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_to_purchase_order/sale_order_to_purchase_order/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_to_purchase_order.listing', {
#             'root': '/sale_order_to_purchase_order/sale_order_to_purchase_order',
#             'objects': http.request.env['sale_order_to_purchase_order.sale_order_to_purchase_order'].search([]),
#         })

#     @http.route('/sale_order_to_purchase_order/sale_order_to_purchase_order/objects/<model("sale_order_to_purchase_order.sale_order_to_purchase_order"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_to_purchase_order.object', {
#             'object': obj
#         })

