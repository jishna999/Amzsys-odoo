from odoo import models, fields, api

class CreatePurchaseOrderWizard(models.TransientModel):
    _name = 'create.purchase.order.wizard'
    _description = 'Wizard to Create Purchase Order from Sale Order'

    vendor_id = fields.Many2one('res.partner', string="Vendor", required=True)
    scheduled_date = fields.Datetime(string="Scheduled Date", default=fields.Datetime.now, required=True)
    order_line_ids = fields.One2many('create.purchase.order.wizard.line', 'wizard_id', string="Order Lines")

    @api.model
    def default_get(self, fields):
        res = super(CreatePurchaseOrderWizard, self).default_get(fields)
        sale_order = self.env['sale.order'].browse(self._context.get('active_id'))
        order_lines = [(0, 0, {
            'product_id': line.product_id.id,
            'product_qty': line.product_uom_qty,
            'price_unit': line.product_id.lst_price,
            'name': line.name,
        }) for line in sale_order.order_line]
        res['order_line_ids'] = order_lines
        return res

    def action_generate_purchase_order(self):
        sale_order = self.env['sale.order'].browse(self._context.get('active_id'))
        purchase_order_vals = {
            'partner_id': self.vendor_id.id,
            'origin': sale_order.name,
            'date_order': fields.Datetime.now(),
            'sale_order_id': sale_order.id,
            'order_line': [
                (0, 0, {
                    'product_id': line.product_id.id,
                    'name': line.name,
                    'product_qty': line.product_qty,
                    'price_unit': line.price_unit,
                    'date_planned': self.scheduled_date,
                }) for line in self.order_line_ids
            ]
        }
        purchase_order = self.env['purchase.order'].create(purchase_order_vals)

        return {
            'type': 'ir.actions.act_window',
            'name': 'Purchase Order',
            'res_model': 'purchase.order',
            'view_mode': 'form',
            'res_id': purchase_order.id,
            'target': 'current',
        }

class CreatePurchaseOrderWizardLine(models.TransientModel):
    _name = 'create.purchase.order.wizard.line'
    _description = 'Wizard Line for Creating Purchase Order'

    wizard_id = fields.Many2one('create.purchase.order.wizard', string="Wizard")
    product_id = fields.Many2one('product.product', string="Product", required=True)
    product_qty = fields.Float(string="Quantity", required=True)
    price_unit = fields.Float(string="Unit Price")
    name = fields.Char(string="Description")
