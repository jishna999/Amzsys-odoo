# -*- coding: utf-8 -*-
# from odoo import http


# class SuggestedProduct(http.Controller):
#     @http.route('/suggested_product/suggested_product', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/suggested_product/suggested_product/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('suggested_product.listing', {
#             'root': '/suggested_product/suggested_product',
#             'objects': http.request.env['suggested_product.suggested_product'].search([]),
#         })

#     @http.route('/suggested_product/suggested_product/objects/<model("suggested_product.suggested_product"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('suggested_product.object', {
#             'object': obj
#         })

