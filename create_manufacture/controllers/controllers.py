# -*- coding: utf-8 -*-
# from odoo import http


# class CreateManufacture(http.Controller):
#     @http.route('/create_manufacture/create_manufacture', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/create_manufacture/create_manufacture/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('create_manufacture.listing', {
#             'root': '/create_manufacture/create_manufacture',
#             'objects': http.request.env['create_manufacture.create_manufacture'].search([]),
#         })

#     @http.route('/create_manufacture/create_manufacture/objects/<model("create_manufacture.create_manufacture"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('create_manufacture.object', {
#             'object': obj
#         })

