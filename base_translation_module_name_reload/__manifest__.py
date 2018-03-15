# -*- coding: utf-8 -*-
# Copyright 2017 Jarvis (www.odoomod.com)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Base Translation Module Name Reload',
    "summary": "Base Translation Module Name Reload",
    "version": "1.0",
    "category": "Localization",
    "website": "http://www.odoomod.com/",
    'description': """
Base Translation Module Name Reload

Usage
1. Activate the developer mode
2. Menu/Settings/Translations/Load a Translation
3. Check "Reload Module Name" and "Load"


使用
1. 激活开发者模式
2. 在菜单/设置/翻译/加载翻译
3. 勾选"重载模块名称"并"加载"

""",
    'author': "Jarvis (www.odoomod.com)",
    'website': 'http://www.odoomod.com',
    'license': 'AGPL-3',
    "depends": [
        'base',
    ],
    "data": [
        'module/wizard/base_language_install_view.xml'
    ],
    'qweb': [
    ],
    'demo': [
    ],
    'css': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
