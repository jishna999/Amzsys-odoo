# -*- coding: utf-8 -*-
# from odoo import http


# class ShowHideProductPrices(http.Controller):
#     @http.route('/show_hide_product_prices/show_hide_product_prices', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/show_hide_product_prices/show_hide_product_prices/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('show_hide_product_prices.listing', {
#             'root': '/show_hide_product_prices/show_hide_product_prices',
#             'objects': http.request.env['show_hide_product_prices.show_hide_product_prices'].search([]),
#         })

#     @http.route('/show_hide_product_prices/show_hide_product_prices/objects/<model("show_hide_product_prices.show_hide_product_prices"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('show_hide_product_prices.object', {
#             'object': obj
#         })

