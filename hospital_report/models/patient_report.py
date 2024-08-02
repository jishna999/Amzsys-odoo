from odoo import models, fields


class PatientReportDetails(models.Model):
    _name = 'patient.report.details'
    _description = 'patient report details'

    patient_id = fields.Many2one(comodel_name='patient.details', string='Patient name')
    doctor_id = fields.Char(string='Doctor name', related='patient_id.appointment_id.doctor_id.name', store=True)
    product_id = fields.Many2one('product.product', string='Medicine')
    price = fields.Float(string='Price')
