# -*- coding: utf-8 -*-
# from odoo import http


# class QuatationReport(http.Controller):
#     @http.route('/quatation_report/quatation_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/quatation_report/quatation_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('quatation_report.listing', {
#             'root': '/quatation_report/quatation_report',
#             'objects': http.request.env['quatation_report.quatation_report'].search([]),
#         })

#     @http.route('/quatation_report/quatation_report/objects/<model("quatation_report.quatation_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('quatation_report.object', {
#             'object': obj
#         })

