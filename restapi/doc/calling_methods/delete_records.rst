Delete Records
==============

.. note:: **API endpoints:**

    * :ref:`DELETE {your_Odoo_server_url}/restapi/1.0/object/{object_name}/{id} <delete-single-record>` (Delete Single Record)
    * :ref:`DELETE {your_Odoo_server_url}/restapi/1.0/object/{object_name}?ids={comma_separated_ids} <delete-record-set>` (Delete Record Set)

.. _delete-single-record:

Delete Single Record
--------------------

Record can be deleted using `unlink() <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.models.Model.unlink>`_, it takes a record id to delete.

.. http:delete:: /restapi/1.0/object/{object_name}/{id}

   **Request**:

   .. sourcecode:: http

      DELETE /restapi/1.0/object/res.partner/20 HTTP/1.1
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

.. _delete-record-set:

Delete List Records
-------------------

Records can be deleted using `unlink() <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.models.Model.unlink>`_, it takes a list of records to delete.

.. http:delete:: /restapi/1.0/object/{object_name}?ids={comma_separated_ids}

   **Request**:

   .. sourcecode:: http

      DELETE /restapi/1.0/object/res.partner?ids=17,20 HTTP/1.1
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