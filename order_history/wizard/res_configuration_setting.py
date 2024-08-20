from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    last_no_of_orders = fields.Integer(
        "Last Number of Orders",
        config_parameter='sale.last_no_of_orders'
    )
    order_stages = fields.Selection(
        [('all', 'All'),
         ('draft', 'Quotation'),
         ('sent', 'Quotation Sent'),
         ('sale', 'Sale Order'),
         ('done', 'Done'),
         ('cancel', 'Cancelled')],
        config_parameter='sale.order_stages',
        string="Order Stages",
        help="Stages of the orders",
        default='all'
    )
    last_no_of_days = fields.Integer(
        "Last Number of Days for Orders",
        config_parameter='sale.last_no_of_days'
    )
    enable_reorder = fields.Boolean(
        "Enable Reorder",
        config_parameter='sale.enable_reorder'
    )