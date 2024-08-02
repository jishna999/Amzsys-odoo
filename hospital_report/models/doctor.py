# -*- coding: utf-8 -*-

from odoo import models, fields


class Doctor(models.Model):
    _name = 'doctor.details'
    _inherit = 'mail.thread'
    _description = 'Displaying doctor details'

    name = fields.Char(string='Doctor name', required=True, tracking=True)
    email = fields.Char(string='Email ID', required=True, tracking=True)
    phone_no = fields.Char(string='Mobile no', required=True, tracking=True)
    department = fields.Selection([('Orthopedist', 'Orthopedist'),
                                   ('General', 'General'),
                                   ('Gynaecology', 'Gynaecology')], string='Department', required=True, tracking=True)
    fee = fields.Float(string='Examination fee', required=True)
    appointment_id = fields.One2many('appointment.details', 'doctor_id', required=True, tracking=True)

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