from odoo import models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'

    suggested_product_ids = fields.One2many(
        comodel_name='suggested.product.line',
        inverse_name='invoice_id',
        string="Suggested Products"
    )
