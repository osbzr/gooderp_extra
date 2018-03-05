# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Enterprise Management Solution
#    risk_management Module
#    Copyright (C) 2014 OpenSur (comercial@opensur.com)
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
    'name': 'Web Menu Hide/Show',
    'category': 'Web',
    'author': 'OpenSur SA',
    'description': """
Web Menu Hide/Show
==================

    * Improves UI by allowing user to hide/show left menu bar

""",
    'version': '1.0',
    'depends': ['web'],
    'data' : [
        'views/web_menu_hide.xml'
    ],
    'qweb' : [
    ],
    'js' : [
        'static/src/js/web_menu_hide.js'
    ],
    'css' : [
        'static/src/css/web_menu_hide.css'
    ],
    'auto_install': False,
    'installable': True,
    'application': True,
}
