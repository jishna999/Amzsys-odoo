# -*- coding: utf-8 -*-
# from odoo import http


# class ProductWizard(http.Controller):
#     @http.route('/product_wizard/product_wizard', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_wizard/product_wizard/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_wizard.listing', {
#             'root': '/product_wizard/product_wizard',
#             'objects': http.request.env['product_wizard.product_wizard'].search([]),
#         })

#     @http.route('/product_wizard/product_wizard/objects/<model("product_wizard.product_wizard"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_wizard.object', {
#             'object': obj
#         })

