from odoo import models, fields, api


class Appointment(models.Model):
    _name = 'appointment.details'
    _inherit = 'mail.thread'
    _description = 'Display appointment details'
    _rec_name = 'doctor_id'

    references = fields.Char(string="References", default="New")
    appointment_date = fields.Date(string='Date', required=True)
    doctor_id = fields.Many2one(comodel_name='doctor.details', required=True)
    patient_id = fields.Many2one(comodel_name='patient.details', required=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('references') or vals['references'] == 'New':
                vals['references'] = self.env['ir.sequence'].next_by_code('appointment.details')
                return super().create(vals_list)

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
