Check Access Rights
===================

For instance to see if we can read the ``res.partner`` model we can call ``check_access_rights`` with ``operation`` passed by position and ``raise_exception`` passed by keyword (in order to get a true/false result rather than true/error).

.. http:get:: /restapi/1.0/object/{object_name}/check_access_rights?operation={list_of_operations}

   **Request**:

   .. sourcecode:: http

      GET /restapi/1.0/object/res.partner/check_access_rights?operation=['read']&raise_exception=True HTTP/1.1
      Host: {your_Odoo_server_url}

   **Response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {
        'return': true
      }

   :query operation: allowed for the user according to the access rights. one of ``create``, ``write``, ``read`` or ``unlink``.
   :query raise_exception: OPTIONAL. raise an ``Error`` or return ``None``, depending
            on the value ``True`` or ``False`` (default: True)
   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :reqheader Authorization: The OAuth protocol parameters to authenticate.                      
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: there’s no resource
   :statuscode 401: authentication failed
   :statuscode 403: if any error raise