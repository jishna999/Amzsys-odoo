from odoo import models, fields


class StudentProfile(models.Model):
    _name = 'student.profile'
    _description = 'Student profile'

    student_name = fields.Char(string='Student name')
    branch_name = fields.Selection([('Computer science', 'Computer science'),

                                    ('Electrical', 'Electrical'),
                                    ('MCA', 'MCA')], string='Branch')
    total_fees = fields.Float(string="Total fees")

    def wiz_open(self):
        return {'type': 'ir.actions.act_window',
                'res_model': 'student.fee.wizard',
                'view_mode': 'form',
                'target': 'new'}

