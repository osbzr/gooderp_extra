Read Records
============

.. note:: **API endpoints:**

    * :ref:`GET {your_Odoo_server_url}/restapi/1.0/object/{object_name}/{id} <read-single-record>` (Read Single Record)
    * :ref:`GET {your_Odoo_server_url}/restapi/1.0/object/{object_name}?ids={comma_separated_ids} <read-record-set>` (Read Record Set)
    * :ref:`GET {your_Odoo_server_url}/restapi/1.0/object/{object_name}/?domain={comma_separated_list_of_args} <read-filter-record>` (Read Filter Records)

.. _read-single-record:

Read Single Record
------------------

Record data is accessible via the `read() <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.models.Model.read>`_, which takes a single record id and optionally a list of fields to fetch. By default, it will fetch all the fields the current user can read, which tends to be a huge amount.

.. http:get:: /restapi/1.0/object/{object_name}/{id}

   **Request**:

   .. sourcecode:: http

      GET /restapi/1.0/object/res.partner/12 HTTP/1.1
      Host: {your_Odoo_server_url}

   **Response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {
        'Partner': {
            'id': 12, 
            'name': 'Think Big Systems',
            'street': '89 Lingfield Tower',
            'street2': false,
            'city': 'London',
            'state_id': false,  
            'zip': false, 
            'country_id': [486, 'United Kingdom'],
            'create_date': '2017-07-10 11:02:57',
            'create_uid': [1, 'Administrator'],
            'write_date': '2017-07-11 15:08:45',
            'write_uid': [1, 'Administrator'],
            ...
            ...
            ...
        }
      }

   :query fields: OPTIONAL. list of field names to return (default is all fields).
   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :reqheader Authorization: The OAuth protocol parameters to authenticate.
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: there’s no resource
   :statuscode 401: authentication failed
   :statuscode 403: if any error raise
   
Conversely, picking only three fields deemed interesting.

   **Request**:

   .. sourcecode:: http

      GET /restapi/1.0/object/res.partner/12?fields=['name','country_id'] HTTP/1.1
      Host: {your_Odoo_server_url}

   **Response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {
        'Partner': {
            'id': 12, 
            'name': 'Think Big Systems',
            'country_id': [486, 'United Kingdom']
        }
      }
      
   .. note:: even if the ``id`` field is not requested, it is always returned
   
.. _read-record-set:

Read List Records
-----------------

Record data is accessible via the `read() <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.models.Model.read>`_, which takes a list of ids (as returned by ``/restapi/1.0/object/{object_name}/search``) and optionally domain filter and a list of fields to fetch. By default, it will fetch all the fields the current user can read, which tends to be a huge amount.

.. http:get:: /restapi/1.0/object/{object_name}?ids={comma_separated_ids}

   **Request**:

   .. sourcecode:: http

      GET /restapi/1.0/object/res.partner?ids=12,17 HTTP/1.1
      Host: {your_Odoo_server_url}

   **Response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {
        'Partner': [
            {
                'id': 12, 
                'name': 'Think Big Systems',
                'street': '89 Lingfield Tower',
                'street2': false,
                'city': 'London',
                'state_id': false,  
                'zip': false, 
                'country_id': [486, 'United Kingdom'],
                'create_date': '2017-07-10 11:02:57',
                'create_uid': [1, 'Administrator'],
                'write_date': '2017-07-11 15:08:45',
                'write_uid': [1, 'Administrator'],
                ...
                ...
                ...
            },
            {
                'id': 17, 
                'name': 'Edward Foster',
                'street': '69 rue de Namur',
                'street2': false,
                'city': 'Wavre',
                'state_id': false,  
                'zip': '1300', 
                'country_id': [274, 'Belgium'],
                'create_date': '2017-07-04 18:10:31',
                'create_uid': [1, 'Administrator'],
                'write_date': '2017-07-04 19:02:59',
                'write_uid': [1, 'Administrator'],
                ...
                ...
                ...
            }
        ]
      }
      
   :query fields: OPTIONAL. list of field names to return (default is all fields).
   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :reqheader Authorization: The OAuth protocol parameters to authenticate.
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: there’s no resource
   :statuscode 401: authentication failed
   :statuscode 403: if any error raise
   
Conversely, picking only three fields deemed interesting.

   **Request**:

   .. sourcecode:: http

      GET /restapi/1.0/object/res.partner?ids=12,17&fields=['name','country_id'] HTTP/1.1
      Host: {your_Odoo_server_url}

   **Response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {
        'Partner': [
            {
                'id': 12, 
                'name': 'Think Big Systems',
                'country_id': [486, 'United Kingdom']
            },
            {
                'id': 17, 
                'name': 'Edward Foster',
                'country_id': [274, 'Belgium']
            }
        ]
      }
      
   .. note:: even if the ``id`` field is not requested, it is always returned
   
.. _read-filter-record:

Read Filter Records
-------------------

Record data is accessible via the ``search_read()`` (shortcut which as its name suggests is equivalent to a `search() <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.models.Model.search>`_ followed by a `read() <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.models.Model.read>`_, but avoids having to perform two requests and keep ids around). 

It takes similar arguments of `search() <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.models.Model.search>`_ and optionally a list of fields to fetch. By default, it will fetch all the records and relavent fields the current user can read, which tends to be a huge amount.

.. http:get:: /restapi/1.0/object/{object_name}/?domain={comma_separated_list_of_args}

   **Request**:

   .. sourcecode:: http

      GET /restapi/1.0/object/res.partner?domain=[('is_company','=',True),('customer','=',True)] HTTP/1.1
      Host: {your_Odoo_server_url}

   **Response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {
        'Partner': [
            {
                'id': 12, 
                'name': 'Think Big Systems',
                'street': '89 Lingfield Tower',
                'street2': false,
                'city': 'London',
                'state_id': false,  
                'zip': false, 
                'country_id': [486, 'United Kingdom'],
                'create_date': '2017-07-10 11:02:57',
                'create_uid': [1, 'Administrator'],
                'write_date': '2017-07-11 15:08:45',
                'write_uid': [1, 'Administrator'],
                ...
                ...
                ...
            },
            {
                'id': 17, 
                'name': 'Edward Foster',
                'street': '69 rue de Namur',
                'street2': false,
                'city': 'Wavre',
                'state_id': false,  
                'zip': '1300', 
                'country_id': [274, 'Belgium'],
                'create_date': '2017-07-04 18:10:31',
                'create_uid': [1, 'Administrator'],
                'write_date': '2017-07-04 19:02:59',
                'write_uid': [1, 'Administrator'],
                ...
                ...
                ...
            },
            ...
            ...
            ...
        ]
      }

   :query domain: OPTIONAL. `A search domain <https://www.odoo.com/documentation/10.0/reference/orm.html#reference-orm-domains>`_. Use an empty
                     list to match all records.
   :query fields: OPTIONAL. list of field names to return (default is all fields).
   :query offset: OPTIONAL. Number of results to ignore (default: none)
   :query limit: OPTIONAL. Maximum number of records to return (default: all)
   :query order: OPTIONAL. Sort string
   :query count: OPTIONAL. if True, only counts and returns the number of matching records (default: False)
   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :reqheader Authorization: The OAuth protocol parameters to authenticate.
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: there’s no resource
   :statuscode 401: authentication failed
   :statuscode 403: if any error raise

Conversely, picking only three fields deemed interesting.

   **Request**:

   .. sourcecode:: http

      GET /restapi/1.0/object/res.partner?domain=[('is_company','=',True),('customer','=',True)]&fields=['name','country_id']&limit=5 HTTP/1.1
      Host: {your_Odoo_server_url}

   **Response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {
        'Partner': [
            {
                'id': 7, 
                'name': 'Agrolait',
                'country_id': [274, 'Belgium']
            },
            {
                'id': 12, 
                'name': 'Think Big Systems',
                'country_id': [486, 'United Kingdom']
            },
            {
                'id': 17, 
                'name': 'Edward Foster',
                'country_id': [274, 'Belgium']
            },
            {
                'id': 8, 
                'name': 'China Export',
                'country_id': [302, 'China']
            },
            {
                'id': 10, 
                'name': 'The Jackson Group',
                'country_id': [488, 'United States']
            }
        ]
      }
      
   .. note:: even if the ``id`` field is not requested, it is always returned