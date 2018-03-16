Count Records
=============

Rather than retrieve a possibly gigantic list of records and count them, `search_count() <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.models.Model.search_count>`_ can be used to retrieve only the number of records matching the query. It takes the same `domain <https://www.odoo.com/documentation/10.0/reference/orm.html#reference-orm-domains>`_ filter as `search() <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.models.Model.search>`_ and no other parameter.

.. warning:: calling ``restapi/1.0/object/{object_name}/search`` then ``restapi/1.0/object/{object_name}/search_count`` (or the other way around) may not yield coherent results if other users are using the server: stored data could have changed between the calls

.. http:get:: /restapi/1.0/object/{object_name}/search_count

   **Request**:

   .. sourcecode:: http

      GET /restapi/1.0/object/res.partner/search_count?domain=[('is_company','=',True),('customer','=',True)] HTTP/1.1
      Host: {your_Odoo_server_url}

   **Response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {
        'count': 19
      }

   :query domain: `A search domain <https://www.odoo.com/documentation/10.0/reference/orm.html#reference-orm-domains>`_. Use an empty
                     list to match all records.
   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :reqheader Authorization: The OAuth protocol parameters to authenticate.
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: there’s no resource
   :statuscode 401: authentication failed
   :statuscode 403: if any error raise