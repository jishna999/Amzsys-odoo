from datetime import timedelta
from odoo import models, fields, api
from odoo.exceptions import UserError


class MrpManufacture(models.TransientModel):
    _name = 'mrp.manufacture'
    _description = 'Wizard to Create and View Manufacture'

    mrp_id = fields.Many2one('mrp.bom', string='Bill of Materials', required=True,readonly=True)
    mrp_line_ids = fields.One2many(
        comodel_name='mrp.manufacture.line',
        inverse_name='manufacture_id',
        string='Manufacture Details'
    )

    @api.model
    def default_get(self, fields_list):
        res = super(MrpManufacture, self).default_get(fields_list)
        mrp_id = self._context.get('default_mrp_bill_of_materials_id')
        if mrp_id:
            res.update({'mrp_id': mrp_id})
        return res

    def action_create_manufacture(self):
        bom = self.mrp_id
        if not bom.product_id:
            raise UserError("The selected Bill of Materials does not have a product associated.")

        manufacturing_orders = []
        for line in self.mrp_line_ids:
            if line.product_qty <= 0:
                raise UserError(f"Invalid quantity for product {bom.product_id.name}.")

            mo_value = {
                'product_id': bom.product_id.id,
                'bom_id': bom.id,
                'product_qty': line.product_qty,
                'date_start': line.date_start,
                'user_id': line.user_id.id
            }
            manufacturing_order = self.env['mrp.production'].create(mo_value)
            manufacturing_orders.append(manufacturing_order.id)

        return {
            'type': 'ir.actions.act_window',
            'name': 'Manufacturing Orders',
            'view_mode': 'tree,form',
            'res_model': 'mrp.production',
            'domain': [('id', 'in', manufacturing_orders)],
            'target': 'current',
        }

