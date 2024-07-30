
from odoo import models, fields


class Patient(models.Model):
    _name = 'patient.details'
    _inherit = 'mail.thread'
    _description = 'Display details of patients'

    name = fields.Char(string='Patient name', tracking=True)
    disease_name = fields.Char(string='Disease name', tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    phone_no = fields.Char(string='Mobile no', tracking=True)
    address = fields.Text(string='Address', tracking=True)
    appointment_id = fields.One2many(comodel_name='appointment.details', inverse_name='patient_id', tracking=True)
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('ongoing', 'Ongoing'), ('done', 'Done'), ('cancel', 'Canceled')], default='draft',
                             tracking=True)

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_ongoing(self):
        for rec in self:
            rec.state = 'ongoing'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'
