from odoo import models, fields, api
from odoo import _
from odoo.exceptions import ValidationError, UserError


class Student(models.Model):
    _name = 'academy.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    mark = fields.Integer(string='Mark')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    qualification = fields.Selection([
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('phd', 'PhD')
    ], string='Qualification')
    teacher_id = fields.Many2one('academy.teacher', string='Teacher')
    state = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    ], string='State', default='new')
    tag_ids = fields.Many2many('academy.student.tag', string='Tags')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals['name']:
                raise ValidationError(" Please provide a valid name.")
        return super(Student, self).create(vals_list)

    def unlink(self):
        for rec in self:
            teacher_domain = [('teacher_id', '=', rec.id)]

            teacher = self.env['academy.teacher'].search(teacher_domain)
            print("msg", teacher_domain)
            if teacher:
                raise ValidationError(_("You cannot delete the teacher now. Students of this teacher exist."))

        # UserError raise invalid operation

        return super().unlink()

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


class Teacher(models.Model):
    _name = 'academy.teacher'
    _description = 'teacher details'

    name = fields.Char(string="Full name")
    phone_no = fields.Char(string="Mobile no")
    department = fields.Char(string="Department")
    address = fields.Text(string="Address")
    student_list = fields.One2many("academy.student", "teacher_id")

    @api.ondelete(at_uninstall=False)
    def delete_teacher(self):
        for rec in self:
            if rec['name'] == 'Raji':
                raise ValidationError(_("You cannot delete the teacher now.Because teacher is HOD"))


class Hobby(models.Model):
    _name = 'academy.hobby'
    _description = 'Hobbies of the students'

    name = fields.Char(string='Hobby')


class StudentTag(models.Model):
    _name = 'student.tag'
    _description = 'Student Tag'
    _rec_names_search = ['mobile']
    _order = 'sequence'

    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer(default=10)
    mobile = fields.Char(string='Mobile')
    student_tag_line_ids = fields.One2many('student.tag.lines', 'student_tag_id')
    total = fields.Float(compute='_compute_total_qty', string='Total Quantity', store=True)

    @api.depends('student_tag_line_ids.qty')
    def _compute_total_qty(self):
        for rec in self:
            rec.total = sum(rec.student_tag_line_ids.mapped('qty'))
            # total_qty = 0
            # for line in rec.student_tag_line_ids:
            #     total_qty += line.qty
            # rec.total = total_qty


class StudentTagLines(models.Model):
    _name = 'student.tag.lines'
    _description = 'Student Tag Lines'

    student_tag_id = fields.Many2one('student.tag', string='Student Tag')
    product_id = fields.Many2one('product.product', string='Student Product')
    qty = fields.Float(string='Quantity')

    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"[{rec.qty}] {rec.student_tag_id.name}"
