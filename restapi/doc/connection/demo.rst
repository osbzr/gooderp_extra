Demo
====

To make exploration simpler, you can also ask https://odoo-restapi-demo.synconics.com for a test database:

.. http:get:: /start

   **Request**:

   .. sourcecode:: http

      GET /start HTTP/1.1
      Host: odoo-restapi-demo.synconics.com

   **Response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {
        'client_id': 'uwCrAHAQbL7D9cvJLIztNaZ0bziEGMDh',
        'client_secret': 'FtHzOQVEs0aSEL9AXuIe9k7X6E2MekU7',
        'host': 'odoo-restapi-demo.synconics.com',
        'database': 'odoo_restapi_demo'
      }
      
   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: there's no resource