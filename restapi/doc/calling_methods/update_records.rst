Update Records
==============

.. note:: **API endpoints:**

    * :ref:`PUT {your_Odoo_server_url}/restapi/1.0/object/{object_name}/{id}?vals={fields_and_values_to_update} <update-single-record>` (Update Single Record)
    * :ref:`PUT {your_Odoo_server_url}/restapi/1.0/object/{object_name}?ids={comma_separated_ids}&vals={fields_and_values_to_update} <update-record-set>` (Update Record Set)

.. _update-single-record:

Update Single Record
--------------------

Record can be updated using `write() <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.models.Model.write>`_, it takes a record id to update and a mapping of updated fields to values similar to `create() <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.models.Model.create>`_.

.. http:put:: /restapi/1.0/object/{object_name}/{id}?vals={fields_and_values_to_update}

   **Request**:

   .. sourcecode:: http

      PUT /restapi/1.0/object/res.partner/20?vals={'street2':'Chung Hsiao East Road'} HTTP/1.1
      Host: {your_Odoo_server_url}

   **Response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {
        'Partner': {
            'id': 20, 
            'name': 'Peter Mitchell',
            'street': '31 Hong Kong street',
            'street2': 'Chung Hsiao East Road',
            'city': 'Taipei',
            'state_id': false,  
            'zip': '106', 
            'country_id': [482, 'Taiwan'],
            'create_date': '2017-07-12 13:34:22',
            'create_uid': [1, 'Administrator'],
            'write_date': '2017-07-13 11:18:28',
            'write_uid': [1, 'Administrator'],
            ...
            ...
            ...
        }
      }

   :query vals: fields to update and the value to set on them:: ``{'field_name': field_value, ...}`` see `write() <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.models.Model.write>`_ for details.
   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :reqheader Authorization: The OAuth protocol parameters to authenticate.
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: there’s no resource
   :statuscode 401: authentication failed
   :statuscode 403: if any error raise

.. _update-record-set:

Update List Records
-------------------

Records can be updated using `write() <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.models.Model.write>`_, it takes a list of records to update and a mapping of updated fields to values similar to `create() <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.models.Model.create>`_.

Multiple records can be updated simultanously, but they will all get the same values for the fields being set. It is not currently possible to perform **computed** updates (where the value being set depends on an existing value of a record).

.. http:put:: /restapi/1.0/object/{object_name}?ids={comma_separated_ids}&vals={fields_and_values_to_update}

   **Request**:

   .. sourcecode:: http

      PUT /restapi/1.0/object/res.partner?ids=17,20&vals={'street2':'Chung Hsiao East Road'} HTTP/1.1
      Host: {your_Odoo_server_url}

   **Response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {
        'Partner': [
            {
                'id': 17, 
                'name': 'Edward Foster',
                'street': '69 rue de Namur',
                'street2': 'Chung Hsiao East Road',
                'city': 'Wavre',
                'state_id': false,  
                'zip': '1300', 
                'country_id': [274, 'Belgium'],
                'create_date': '2017-07-04 18:10:31',
                'create_uid': [1, 'Administrator'],
                'write_date': '2017-07-13 11:18:28',
                'write_uid': [1, 'Administrator'],
                ...
                ...
                ...
            },
            {
                'id': 20, 
                'name': 'Peter Mitchell',
                'street': '31 Hong Kong street',
                'street2': 'Chung Hsiao East Road',
                'city': 'Taipei',
                'state_id': false,  
                'zip': '106', 
                'country_id': [482, 'Taiwan'],
                'create_date': '2017-07-12 13:34:22',
                'create_uid': [1, 'Administrator'],
                'write_date': '2017-07-13 11:18:28',
                'write_uid': [1, 'Administrator'],
                ...
                ...
                ...
            }
        ]
      }

   :query vals: fields to update and the value to set on them:: ``{'field_name': field_value, ...}`` see `write() <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.models.Model.write>`_ for details.
   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :reqheader Authorization: The OAuth protocol parameters to authenticate.
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: there’s no resource
   :statuscode 401: authentication failed
   :statuscode 403: if any error raise