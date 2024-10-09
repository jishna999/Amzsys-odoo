# -*- coding: utf-8 -*-
from addons.account.models.account_journal_dashboard import account_journal
from odoo import models, fields, api


class RegisterPayment(models.TransientModel):
    _name = 'register.payment'

    bill_date = fields.Date(string="Bill date")
    journal_id = fields.Many2one(comode_name='account.journal')

    @api.model
    def default_get(self, fields):
        res = super(RegisterPayment, self).default_get(fields)
        picking_id = self.env.context.get('default_stock_picking_id')
        picking = self.env['stock.picking'].browse(picking_id)
        res.update({'picking_id': 'picking'})

    def action_create_vendor_bill(self):
        picking = self.env['stock.picking'].browse(self._context.get('active_id'))
        purchase_order = picking.purchase_id
        bill_vals = {
            'move_type': 'to_invoice',
            'partner_id': purchase_order.partner_id,
            'invoice_date': self.bill_date,
            'invoice_origin': purchase_order.name,
            'journal_id':self.journal_id.id,
            'invoice_line_ids':[(0,0,{
                'product_id':line.product_id.id,
                'quantity':line.qty_done,
            'purchase_line_id':line.purchase_line_id.id,}) for line in picking.move_lines if line.qty_done>=1]


        }

        create_bill = self.env['account.move'].create(bill_vals)
        picking.write({'bill_id':bill_vals.id})
        purchase_order.write({'bill_ids':[(4,bill_vals.id)]})
        for line in picking.move_lines:
            po_lines = line.purchase_line_id
            po_lines.qty_invoiced=po_lines.qty_invoiced+line.qty_done
        return create_bill
