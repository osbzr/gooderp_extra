# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2017 - odoobiz (<http://www.odoobiz.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Estate Backend Theme',
    'version': '1.0',
    'category': 'Themes/Backend',
    'description': """
Estate Backend Theme
=======================================
This theme has been developed for community version only.

""",
    'author': 'odoobiz',
    'website': 'http://www.odoobiz.com',
    'summary': 'Estate Backend Theme with Foldable Menu',
    'sequence': 20,
    'depends': ['base','web'],
    'data': ['views.xml'],
    'demo': [
    ],
    'test': [
    ],
    'css': [
    ],
    'images': [
    ],
    'application': True,
    'auto_install': False,
    'installable': True,
    'images': ['static/images/main.png'],
    'currency': 'EUR',
    'license': 'OPL-1',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: