.. _create-records:

Create Records
==============

Records of a model are created using `create() <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.models.Model.create>`_.

It takes a mapping of fields to values, used to initialize the record. For any field which has a default value and is not set through the mapping argument, the default value will be used.

.. warning:: while most value types are what would be expected (integer for `Integer <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.fields.Integer>`_, string for `Char <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.fields.Char>`_ or `Text <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.fields.Text>`_), 
    
    * `Date <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.fields.Date>`_, `Datetime <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.fields.Datetime>`_ and ``Binary`` fields use string values
    * `One2many <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.fields.One2many>`_ and `Many2many <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.fields.Many2many>`_ use a special command protocol detailed in `the documentation to the write method <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.models.Model.write>`_.

.. http:post:: /restapi/1.0/object/{object_name}?vals={values_for_the_object's_fields}

   **Request**:

   .. sourcecode:: http

      POST /restapi/1.0/object/res.partner?vals={'name':'Peter Mitchell','street':'31 Hong Kong street','city':'Taipei','zip':'106','country_id':482} HTTP/1.1
      Host: <your Odoo server url>

   **Response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {
        'Partner': {
            'id': 20, 
            'name': 'Peter Mitchell',
            'street': '31 Hong Kong street',
            'street2': false,
            'city': 'Taipei',
            'state_id': false,  
            'zip': '106', 
            'country_id': [482, 'Taiwan'],
            'create_date': '2017-07-12 13:34:22',
            'create_uid': [1, 'Administrator'],
            'write_date': '2017-07-12 13:34:22',
            'write_uid': [1, 'Administrator'],
            ...
            ...
            ...
        }
      }

   :query vals: values for the object's fields, as a dictionary:: ``{'field_name': field_value, ...}`` see `write() <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.models.Model.write>`_ for details.
   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :reqheader Authorization: The OAuth protocol parameters to authenticate.
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: there’s no resource
   :statuscode 401: authentication failed
   :statuscode 403: if any error raise


