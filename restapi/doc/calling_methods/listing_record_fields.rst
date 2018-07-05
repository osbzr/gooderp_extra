.. _listing-record-fields:

Listing Record Fields
=====================

`fields_get() <https://www.odoo.com/documentation/10.0/reference/orm.html#odoo.models.Model.fields_get>`_ can be used to inspect a model's fields and check which ones seem to be of interest.

Because it returns a large amount of meta-information (it is also used by client programs) it should be filtered before printing, the most interesting items for a human user are ``string`` (the field's label), ``help`` (a help text if available) and ``type`` (to know which values to expect, or to send when updating a record).

.. http:get:: /restapi/1.0/object/{object_name}/fields_get

   **Request**:

   .. sourcecode:: http

      GET /restapi/1.0/object/res.partner/fields_get?allfields=[]&attributes=['string','help','type'] HTTP/1.1
      Host: {your_Odoo_server_url}

   **Response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {
        'fields': {
            'ean13': {
                'type': 'char',
                'help': 'BarCode',
                'string': 'EAN13'
            },
            'property_account_position_id': {
                'type': 'many2one',
                'help': 'The fiscal position will determine taxes and accounts used for the partner.',
                'string': 'Fiscal Position'
            },
            'signup_valid': {
                'type': 'boolean',
                'help': '',
                'string': 'Signup Token is Valid'
            },
            'date_localization': {
                'type": 'date',
                'help": '',
                'string': 'Geo Localization Date'
            },
            'ref_company_ids': {
                'type': 'one2many',
                'help': '',
                'string': 'Companies that refers to partner'
            },
            'sale_order_count': {
                'type': 'integer',
                'help': '',
                'string': '# of Sales Order'
            },
            'purchase_order_count': {
                'type': 'integer',
                'help': '',
                'string': '# of Purchase Order'
            }
        }
      }

   :query allfields: OPTIONAL. list of fields to document, all if empty or not provided
   :query attributes: OPTIONAL. list of description attributes to return for each field, all if empty or not provided
   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :reqheader Authorization: The OAuth protocol parameters to authenticate.
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: there’s no resource
   :statuscode 401: authentication failed
   :statuscode 403: if any error raise