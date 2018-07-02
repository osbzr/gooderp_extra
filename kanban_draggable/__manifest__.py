# -*- coding: utf-8 -*-
# © 2018 NavyBits (<http://navybits.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Kanban Drag Drop Control',
    'description': """
Disable DragDrop/Sorting In Specific Kanban View
================================================
 To disable drag drop record between columns add:
 
  disable_drag_drop_record="true" into the <kanban> tag.

 To disable drag drop and sorting records add :

  disable_sort_record="true" into the <kanban> tag.
  
 To disable sorting columns add :

  disable_sort_column="true" into the <kanban> tag.

 Example: 
 
  <kanban disable_sort_column='true' disable_sort_record='true' disable_drag_drop_record='true'>
        
   ...

   ...
        
  </kanban>
    """,

    'version': '1.0',
    'category': 'Extra Tools',
    'summary': 'Provides the ability to control drag drop and sorting behavior in kanban views.',
    'author': 'Mahmoud Fakhreddine,'
              'Navybits',
    "website": "https://navybits.com/",
    'depends': [
        'web',
        'web_kanban',
    ],
    'data': [
        'views/templates.xml',
    ],
    'images': ['images/odoo-listing-kanban-draggable_screenshot.jpg'],

    'installable': True,
    'application': False,
    'auto_install': False,
    'license': "AGPL-3",
}
