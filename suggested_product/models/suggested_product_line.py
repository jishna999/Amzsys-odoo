from odoo import models, fields, api


class SuggestedProductLine(models.Model):
    _name = 'suggested.product.line'

    invoice_id = fields.Many2one(
        comodel_name='account.move',
        string='Invoice'
    )

    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Product',
        domain="[('sale_ok', '=', True)]",
        options={'no_create': True}
    )
    # invoice_suggested_product_ids = fields.Many2many(
    #     comodel_name='sale.order',
    #     relation='suggested_product_invoice_rel',
    #     column1='suggested_product_id',
    #     column2='suggested_line_id',
    #     string='Suggested Product Invoice Lines',
    #     readonly=True,
    #     copy=False
    # )

    product_uom_qty = fields.Float(string='Quantity')
    sale_price = fields.Float(string='Sale Price')

    @api.onchange('product_id')
    def onchange_product_sale_price(self):
        if self.product_id:
            self.sale_price = self.product_id.list_price
        else:
            self.sale_price = 0.0
