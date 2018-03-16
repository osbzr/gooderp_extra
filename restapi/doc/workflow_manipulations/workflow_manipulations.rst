Workflow Manipulations
======================

`Workflows <https://www.odoo.com/documentation/10.0/reference/workflows.html#reference-workflows>`_ can be moved along by sending them signals.

Signals are sent to a specific record using ``restapi/1.0/workflow`` endpoint, and possibly trigger a transition on the workflow instance associated with the record.

.. http:get:: /restapi/1.0/workflow/{object_name}/{id}/{signal}

   **Request**:
   
   .. warning:: this example needs ``account`` module installed

   .. sourcecode:: http

      GET /restapi/1.0/workflow/account.invoice/5/invoice_open HTTP/1.1
      Host: {your_Odoo_server_url}

   **Response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {}
      
   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :reqheader Authorization: The OAuth protocol parameters to authenticate.
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: there’s no resource
   :statuscode 401: authentication failed
   :statuscode 403: if any error raise