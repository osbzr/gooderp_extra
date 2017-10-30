# -*- coding: utf-8 -*-
{
    'name': "Web Select List View Column",

    'summary': """
        To enable user customizing (hide or show) list view columns.
    """,

    'description': """
        To enable user customizing (hide or show) list view columns, also the configuration can be saved and reset.
    """,

    'author': "MAXodoo",
    'website': "http://www.maxodoo.com",
    'category': 'web',
    'version': '10.0.0.1',
    'depends': ['web'],
    'data': [
        'security/ir.model.access.csv',
        'views/max_web_select_list_view_column_view.xml',
    ],
    'qweb': ['static/src/xml/list_view_button_view.xml'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
