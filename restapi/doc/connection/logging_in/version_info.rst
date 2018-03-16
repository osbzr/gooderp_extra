Odoo Version Information
========================

The ``restapi/1.0/common/version`` endpoint provides Odoo server version information which don't require authentication.

.. http:get:: /restapi/1.0/common/version

   **Request**:

   .. sourcecode:: http

      GET /restapi/1.0/common/version HTTP/1.1
      Host: <your Odoo server url>

   **Response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {
        'server_version': '8.0',
        'server_version_info': [8, 0, 0, "final", 0],
        'server_series': '8.0',
        'protocal_version': 1
      }

   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: there's no user