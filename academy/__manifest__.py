{
    'name': "academy",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'mail', 'product'],

    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/hobbi.xml',
        'views/student_tag.xml',
        'views/student_tag_lines.xml',
        'views/student_tag_line_views.xml',
        'views/data.xml',

    ],

    'demo': [
        'demo/demo.xml',
    ],
}
