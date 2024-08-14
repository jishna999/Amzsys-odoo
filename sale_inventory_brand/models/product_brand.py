from odoo import models, fields


class ProductBrand(models.Model):
    _name = 'product.brand'
    _description = 'brand name'
    _rec_name = 'brand_name'

    brand_name = fields.Char(string='Brand Name')


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    brand_id = fields.Many2one('product.brand', string='Brand')
