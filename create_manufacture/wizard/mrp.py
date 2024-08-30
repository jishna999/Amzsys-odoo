from datetime import timedelta
from odoo import models, fields, api
from odoo.exceptions import UserError

class MrpManufacture(models.TransientModel):
    _name = 'mrp.manufacture'
    _description = 'Wizard to Create and View Manufacture'

    mrp_id = fields.Many2one('mrp.bom', string='Bill of Materials', required=True)
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

        mo_value = {
            'product_id': bom.product_id.id,
            'bom_id': bom.id,
            'product_qty': self.mrp_line_ids.product_qty ,
            'date_start': self.mrp_line_ids.date_start,
            'user_id': self.mrp_line_ids[0].user_id.id
        }

        manufacturing_order = self.env['mrp.production'].create(mo_value)

        manufacturing_order.action_assign()
        manufacturing_order.button_plan()

        return {
            'type': 'ir.actions.act_window',
            'name': 'Manufacturing Order',
            'view_mode': 'form',
            'res_model': 'mrp.production',
            'res_id': manufacturing_order.id,
            'target': 'current',
        }


class MrpManufactureLine(models.TransientModel):
    _name = 'mrp.manufacture.line'
    _description = 'Wizard Line for Creating Manufacture'

    manufacture_id = fields.Many2one(
        'mrp.manufacture',
        string='Manufacture',
        readonly=True,
        ondelete='cascade'
    )
    product_id = fields.Many2one('product.product', string='Product', required=True)
    product_qty = fields.Float(string='Product Quantity', required=True)
    date_start = fields.Datetime(string='Scheduled Date', default=fields.Datetime.now)
    date_finished = fields.Datetime(string='End Date', readonly=True, compute='_compute_date_finished', store=True)
    user_id = fields.Many2one('res.users', string='Responsible User', required=True)

    @api.depends('date_start')
    def _compute_date_finished(self):
        for record in self:
            record.date_finished = record.date_start + timedelta(
                hours=1) if record.date_start else fields.Datetime.now() + timedelta(hours=1)

    @api.model
    def create(self, vals):
        vals.setdefault('date_start', fields.Datetime.now())
        vals['date_finished'] = fields.Datetime.from_string(vals['date_start']) + timedelta(hours=1)
        return super(MrpManufactureLine, self).create(vals)