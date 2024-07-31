from odoo import models, fields


class AddRegistration(models.Model):
    _inherit = 'account.move'

    follow_date = fields.Date(string='Follow Date')

    def edit_button(self):
        for record in self:
            record.message_post(body="Edit button clicked")
        return True
