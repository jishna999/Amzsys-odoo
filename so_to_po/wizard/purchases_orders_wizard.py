from odoo import models, fields, api, exceptions

class CreatePurchaseOrderWizard(models.TransientModel):
    _name = 'create.purchase.order.wizard'
    _description = 'Wizard to Create Purchase Orders from Sale Order'

    vendor_id = fields.Many2one('res.partner', string="Vendor",  required=True)
    scheduled_date = fields.Date(string="Scheduled Date", required=True)
    sale_order_line_ids = fields.Many2many('sale.order.line', string="Sale Order Lines", required=True)

    @api.model
    def default_get(self, fields):
        res = super(CreatePurchaseOrderWizard, self).default_get(fields)
        sale_order_id = self.env.context.get('default_sale_order_id')
        if sale_order_id:
            sale_order = self.env['sale.order'].browse(sale_order_id)
            res.update({
                'sale_order_line_ids': [(6, 0, sale_order.order_line.ids)],
            })
        return res

    def create_purchase_orders(self):
        sale_order = self.env['sale.order'].browse(self.env.context.get('active_id'))
        if not self.sale_order_line_ids:
            raise exceptions.UserError("You must select at least one sale order line.")

        purchase_order = self.env['purchase.order'].create({
            'partner_id': self.vendor_id.id,
            'sale_order_id': sale_order.id,
            'date_planned': self.scheduled_date,
        })

        for line in self.sale_order_line_ids:
            self.env['purchase.order.line'].create({
                'order_id': purchase_order.id,
                'product_id': line.product_id.id,
                'name': line.name,
                'product_qty': line.product_uom_qty,
                'price_unit': line.price_unit,
                'date_planned': self.scheduled_date,
            })

        sale_order.purchase_ids |= purchase_order
        return {'type': 'ir.actions.act_window_close'}
