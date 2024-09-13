# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseOrderFromSaleOrder(http.Controller):
#     @http.route('/purchase_order_from_sale_order/purchase_order_from_sale_order', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_order_from_sale_order/purchase_order_from_sale_order/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_order_from_sale_order.listing', {
#             'root': '/purchase_order_from_sale_order/purchase_order_from_sale_order',
#             'objects': http.request.env['purchase_order_from_sale_order.purchase_order_from_sale_order'].search([]),
#         })

#     @http.route('/purchase_order_from_sale_order/purchase_order_from_sale_order/objects/<model("purchase_order_from_sale_order.purchase_order_from_sale_order"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_order_from_sale_order.object', {
#             'object': obj
#         })

