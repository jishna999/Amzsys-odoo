# -*- coding: utf-8 -*-
# from odoo import http


# class HospitalReport(http.Controller):
#     @http.route('/hospital_report/hospital_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospital_report/hospital_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital_report.listing', {
#             'root': '/hospital_report/hospital_report',
#             'objects': http.request.env['hospital_report.hospital_report'].search([]),
#         })

#     @http.route('/hospital_report/hospital_report/objects/<model("hospital_report.hospital_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital_report.object', {
#             'object': obj
#         })

