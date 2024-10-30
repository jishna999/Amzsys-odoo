from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    vendor_bill_ids = fields.Many2many(
        'account.move',
        string="Vendor Bills",
        readonly=True,
        domain=[('move_type', '=', 'in_invoice')]
    )

    invoice_count = fields.Integer(
        string="Vendor Bill Count",
        compute="_compute_invoice_count",
        store=True,
    )

    @api.depends('vendor_bill_ids')
    def _compute_invoice_count(self):
        for picking in self:
            picking.invoice_count = len(picking.vendor_bill_ids)

    def action_view_invoice(self):

        if self.purchase_id:
            res = self.purchase_id.action_view_invoice()
            return res
        # result = self.env['ir.actions.act_window']._for_xml_id('account.action_move_in_invoice_type')
        # return result
        #

