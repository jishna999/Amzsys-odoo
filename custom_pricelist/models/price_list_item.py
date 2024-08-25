from pkg_resources import require

from odoo import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)


class ProductPricelistItem(models.Model):
    _inherit = 'product.pricelist.item'

    compute_price = fields.Selection(
        selection_add=[('tiered', 'Tiered')],
        ondelete={'tiered': 'set default'}
    )
    tiers_ids = fields.One2many(
        comodel_name='tiers.lines',
        inverse_name='pricelist_item_id',
        string='Tiers'
    )
    product_variant_ids = fields.Many2one(
        comodel_name='product.product',
        string="Product Variant",
        ondelete='cascade',require=True,
        help="Specify the product variant if this rule only applies to a specific product variant. Leave empty otherwise."
    )

    @api.depends('compute_price', 'tiers_ids')
    def _compute_name_and_price(self):

        for item in self:
            super(ProductPricelistItem, item)._compute_name_and_price()

            if item.compute_price == 'tiered' and item.product_variant_ids and item.tiers_ids:

                item.price = _("%s tiers defined: %s") % (
                    len(item.tiers_ids),
                    ','.join(map(str, item.tiers_ids.mapped('tier_no')))
                )
                item.name = ', '.join(item.product_variant_ids.mapped('name'))


            else:
                item.price = _("No tiers defined")
                item.name = ''


class ProductProduct(models.Model):
    _inherit = 'product.product'

    pricelist_item_ids = fields.One2many(
        comodel_name='product.pricelist.item',
        inverse_name='product_variant_ids',
        string='Pricelist Items'
    )


class TiersLines(models.Model):
    _name = 'tiers.lines'
    _description = 'Tiers Lines'

    pricelist_item_id = fields.Many2one(
        comodel_name='product.pricelist.item',
        string='Pricelist Item',
        ondelete='cascade',
        required=True
    )
    tier_no = fields.Integer(string='Tier ID', default=1)
    tier_from = fields.Float(string='Min Quantity')
    tier_to = fields.Float(string='Max Quantity')
    list_price = fields.Monetary(
        string='List Price',
        currency_field='currency_id'
    )
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        required=True,
        default=lambda self: self.env.company.currency_id
    )


