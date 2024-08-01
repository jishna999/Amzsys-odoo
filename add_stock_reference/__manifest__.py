# -*- coding: utf-8 -*-
{
    'name': "add_stock_reference",

    'summary': "add stock_preference field in sale.order to stock.picking",

    'description': """
Add new field
    """,
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['sale','stock','stock_account','sale_management','custom_sales'],
    'data': [
        'security/ir.model.access.csv',
        'views/add_stock_reference.xml',
        'views/stock_move_template.xml'
    ],
    'demo': [
        'demo/demo.xml',
    ],
}

