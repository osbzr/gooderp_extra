Inspection and Introspection
============================

While we previously used `fields_get() <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.models.Model.fields_get>`_ to query a model and have been using an arbitrary model from the start, Odoo stores most model metadata inside a few meta-models which allow both querying the system and altering models and fields (with some limitations) on the fly over REST API.

.. note::

    1. :ref:`Provides information about Odoo models via its various fields <ir-model>` (ir.model)
    2. :ref:`Provides information about the fields of Odoo models and allows adding custom fields without using Python code <ir-model-fields>` (ir.model.fields)

.. _ir-model:

ir.model
--------

Provides information about Odoo models via its various fields

name
    a human-readable description of the model
model
    the name of each model in the system
state
    whether the model was generated in Python code (``base``) or by creating an ``ir.model`` record (``manual``)
field_id
    list of the model's fields through a `One2many <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.fields.One2many>`_ to :ref:`ir-model-fields`
view_ids
    `One2many <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.fields.One2many>`_ to the `Views <https://www.odoo.com/documentation/10.0/reference/views.html#reference-views>`_ defined for the model
access_ids
    `One2many <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.fields.One2many>`_ relation to the `Access Control <https://www.odoo.com/documentation/10.0/reference/security.html#reference-security-acl>`_ set on the model
    
.. note:: ``ir.model`` can be used to:

    * query the system for installed models (as a precondition to operations on the model or to explore the system's content)
    * get information about a specific model (generally by listing the fields associated with it)
    * create new models dynamically over REST API
    
.. warning:: * **custom** model names must start with ``x_``
    * the ``state`` must be provided and ``manual``, otherwise the model will not be loaded
    * it is not possible to add new `methods` to a custom model, only fields
    

Example
~~~~~~~

1. Create ``x_custom_model`` model record in ``ir.model`` object using :ref:`create-records` API endpoint.

   **Request**:

   .. sourcecode:: http

      POST /restapi/1.0/object/ir.model?vals={'name':'Custom Model','model':'x_custom_model','state':'manual'} HTTP/1.1
      Host: {your_Odoo_server_url}

   **Response**: 

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {
        'Models': {
            'id': 104, 
            'name': 'Custom Model',
            'model': 'x_custom_model',
            'state': 'manual'
            ...
            ...
            ...
        }
      }
      
2.  Inspect a model ``x_custom_model``’s fields using :ref:`listing-record-fields` API endpoint.

   **Request**:

   .. sourcecode:: http

      GET /restapi/1.0/object/x_custom_model/fields_get?attributes=['string','help','type'] HTTP/1.1
      Host: {your_Odoo_server_url}

   **Response**: 
   
   .. note:: a custom model will initially contain only the "built-in" fields available on all models 

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {
        'fields': {
            'create_uid': {
                'type': 'many2one',
                'string': 'Created by'
            },
            'create_date': {
                'type": 'datetime',
                'string': 'Created on'
            },
            '__last_update': {
                'type': 'datetime',
                'string': 'Last Modified on'
            },
            'write_uid': {
                'type': 'many2one',
                'string': 'Last Updated by'
            },
            'write_date': {
                'type': 'datetime',
                'string': 'Last Updated on'
            },
            'display_name': {
                'type': 'char',
                'string': 'Display Name'
            },
            'id": {
                'type': 'integer',
                'string': 'Id'
            }
        }
     }
     
.. _ir-model-fields:

ir.model.fields
---------------

Provides information about the fields of Odoo models and allows adding custom fields without using Python code

model_id
    `Many2one <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.fields.Many2one>`_ to :ref:`ir-model` to which the field belongs
name
    the field's technical name (used in ``read`` or ``write``)
field_description
    the field's user-readable label (e.g. ``string`` in ``fields_get``)
ttype
    the `type <https://www.odoo.com/documentation/10.0/reference/orm.html#reference-orm-fields>`_ of field to create
state
    whether the field was created via Python code (``base``) or via ``ir.model.fields`` (``manual``)
required, readonly, translate
    enables the corresponding flag on the field
groups
    `field-level access control <https://www.odoo.com/documentation/10.0/reference/security.html#reference-security-fields>`_, a `Many2many <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.fields.Many2many>`_ to ``res.groups``
selection, size, on_delete, relation, relation_field, domain
    type-specific properties and customizations, see `the fields documentation <https://www.odoo.com/documentation/10.0/reference/orm.html#reference-orm-fields>`_ for details
    
.. note:: Like custom models, only new fields created with ``state="manual"`` are activated as actual fields on the model.

.. warning:: computed fields can not be added via ``ir.model.fields``, some field meta-information (defaults, onchange) can not be set either

Example
~~~~~~~

1. Create ``x_custom`` model record in ``ir.model`` object using :ref:`create-records` API endpoint.

   **Request**:

   .. sourcecode:: http

      POST /restapi/1.0/object/ir.model?vals={'name':'Custom Model','model':'x_custom','state':'manual'} HTTP/1.1
      Host: {your_Odoo_server_url}

   **Response**: 

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {
        'Models': {
            'id': 105, 
            'name': 'Custom Model',
            'model': 'x_custom',
            'state': 'manual'
            ...
            ...
            ...
        }
      }
      
2. Create ``x_name`` field record in ``ir.model.fields`` object using :ref:`create-records` API endpoint.

   **Request**:

   .. sourcecode:: http

      POST /restapi/1.0/object/ir.model.fields?vals={'model_id':105,'name':'x_name','ttype':'char','state':'manual','required':True} HTTP/1.1
      Host: {your_Odoo_server_url}

   **Response**: 

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {
        'Fields': {
            'id': 210, 
            'name': 'x_name',
            'model_id': [105, 'Custom Model'],
            'ttype': 'char', 
            'state': 'manual',
            'required': True 
            ...
            ...
            ...
        }
      }
      
3. Create ``test record`` record in ``x_custom`` object using :ref:`create-records` API endpoint.

   **Request**:

   .. sourcecode:: http

      POST /restapi/1.0/object/x_custom?vals={'x_name':'test record'} HTTP/1.1
      Host: {your_Odoo_server_url}

   **Response**: 

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {
        'Custom Model': {
            'id': 115, 
            'x_name': 'test record',
            'display_name': 'test record',            
            'create_date': '2017-07-15 14:31:17',
            'create_uid': [1, 'Administrator'],
            'write_date': '2017-07-15 14:31:17',
            'write_uid': [1, 'Administrator'],
            ...
            ...
            ...
        }
      }