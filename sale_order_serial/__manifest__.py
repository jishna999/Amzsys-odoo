# -*- coding: utf-8 -*-
{
    'name': "sale_order_serial",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'custom_sales', 'account', 'stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order_template_lot_ids.xml',
        'views/account_move_template.xml',
        # 'views/stock_move_line__lot_is_template.xml',
        # 'views/stock_move_template_lot_ids.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
