from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    last_no_of_orders = fields.Integer("Last Number of Orders")
    order_stages = fields.Selection(
        [('all', 'All'),
         ('draft', 'Draft'),
         ('sent', 'Sent'),
         ('sale', 'Sale'),
         ('done', 'Done'),
         ('cancel', 'Cancelled'), ],
        string="Order Stages",
        help="Stages of the orders",
        default='all'
    )
    last_no_of_days = fields.Integer("Last Number of Days for Orders")
    enable_reorder = fields.Boolean("Enable Reorder")

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()

        res.update(
            last_no_of_orders=int(self.env['ir.config_parameter'].sudo().get_param('sale.last_no_of_orders', default=0)),
            order_stages=self.env['ir.config_parameter'].sudo().get_param('sale.order_stages', default='all'),
            last_no_of_days=int(self.env['ir.config_parameter'].sudo().get_param('sale.last_no_of_days', default=0)),
            enable_reorder=self.env['ir.config_parameter'].sudo().get_param('sale.enable_reorder', default=False) == 'True'
        )
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()

        self.env['ir.config_parameter'].sudo().set_param('sale.last_no_of_orders', self.last_no_of_orders)
        self.env['ir.config_parameter'].sudo().set_param('sale.order_stages', self.order_stages)
        self.env['ir.config_parameter'].sudo().set_param('sale.last_no_of_days', self.last_no_of_days)
        self.env['ir.config_parameter'].sudo().set_param('sale.enable_reorder', str(self.enable_reorder))

    def execute(self):
        res1 = super(ResConfigSettings, self).execute()
        return res1
