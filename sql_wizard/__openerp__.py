# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'sql wizard',
    'version': '1.0',
    'website': 'http://www.csfinox.cn',
    'category': 'dayuan',
    'author': 'Jerry Luo',
    'sequence': 200,
    'summary': 'sql wizard',
    'depends': ['base'],
    'description': """
sql wizard,

    """,
    'data': [
      'wizard/sql_wizard.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
