List Records
============

Records can be listed and filtered via `search() <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.models.Model.search>`_. It takes a mandatory `domain <https://www.odoo.com/documentation/10.0/reference/orm.html#reference-orm-domains>`_ filter (possibly empty), and returns the database identifiers of all records matching the filter.

.. http:get:: /restapi/1.0/object/{object_name}/search

   **Request**:

   .. sourcecode:: http

      GET /restapi/1.0/object/res.partner/search?domain=[('is_company','=',True),('customer','=',True)] HTTP/1.1
      Host: {your_Odoo_server_url}

   **Response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {
        'Partner': [
            7, 18, 12, 10, 17, 19, 8, 31, 26, 16, 13, 20, 30, 22, 29, 15, 23, 28, 74
        ]
      }

   :query domain: `A search domain <https://www.odoo.com/documentation/10.0/reference/orm.html#reference-orm-domains>`_. Use an empty
                     list to match all records.
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
   
   
Pagination
----------

By default a ``restapi/1.0/object/{object_name}/search`` will return the ids of all records matching the condition, which may be a huge number. ``offset`` and ``limit`` parameters are available to only retrieve a subset of all matched records.

   **Request**:

   .. sourcecode:: http

      GET /restapi/1.0/object/res.partner/search?domain=[('is_company','=',True),('customer','=',True)]&offset=10&limit=5 HTTP/1.1
      Host: {your_Odoo_server_url}

   **Response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {
        'Partner': [
            13, 20, 30, 22, 29
        ]
      }