Report Printing
===============

Available reports can be listed by searching the ``ir.actions.report.xml`` model, fields of interest being

model
    the model on which the report applies, can be used to look for available reports on a specific model
    
name
    human-readable report name
    
report_name
    the technical name of the report, used to print it

Reports can be printed using ``restapi/1.0/report`` endpoint over REST API with the following information:

    * the name of the report (``report_name``)
    * the single record id or ids of the records to include in the report

.. note:: **API endpoints:**

    * :ref:`GET {your_Odoo_server_url}/restapi/1.0/report/{report_name}/{id} <print-single-report>` (Print Single Report)
    * :ref:`GET {your_Odoo_server_url}/restapi/1.0/report/{report_name}?ids={comma_separated_ids} <print-report-set>` (Print Report Set)

.. _print-single-report:

Print Single Report
-------------------

Report can be printed by giving the name of the report(``report_name``) and a single record id.

.. http:get:: /restapi/1.0/report/{report_name}/{id}

   **Request**:
   
   .. warning:: this example needs ``account`` module installed  

   .. sourcecode:: http

      GET /restapi/1.0/report/account.report_invoice/12 HTTP/1.1
      Host: {your_Odoo_server_url}

   **Response**: 
   
   .. note:: the report is sent as PDF binary data encoded in `base64 <https://en.wikipedia.org/wiki/Base64>`_, it must be decoded and may need to be saved to disk before use

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {
        'report': {
            'id': 12, 
            'state': 'true',
            'format': 'pdf',
            'result': 'R0lGODlhbgCMAPf\/APbr48VySrxTO7IgKt2qmKQdJeK8lsFjROG5p\
            /nz7Zg3\nMNmnd7Q1MLNVS9GId71hSJMZIuzTu4UtKbeEeakhKMl8U8WYjfr18YQaIbAf\n
            KKwhKdKzqpQtLebFortOOejKrOjZ1Mt7aMNpVbAqLLV7bsNqR+3WwMqEWenN\n
            sZYxL\/Ddy\/Pm2e7ZxLlUQrIjNPXp3bU5MbhENbEtLtqhj5ZQTfHh0bMxL7Ip\n
            NsNyUYkZIrZJPcqGdYIUHb5aPKkeJnoUHd2yiJkiLKYiKLRFOsyJXKVDO8up\n
            osFaS+TBnK4kKti5sNaYg\/z49aqYl5kqLrljUtORfMOlo\/36+H4ZH
            ...
            ...
            ...'
        }
      }
      
   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :reqheader Authorization: The OAuth protocol parameters to authenticate.
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: there’s no resource
   :statuscode 401: authentication failed
   :statuscode 403: if any error raise
   
.. _print-report-set:

Print List Reports
------------------

Report can be printed by giving the name of the report(``report_name``) and a list of records.

.. http:get:: /restapi/1.0/report/{report_name}?ids={comma_separated_ids}

   **Request**:
   
   .. warning:: this example needs ``account`` module installed  

   .. sourcecode:: http

      GET /restapi/1.0/report/account.report_invoice?ids=12,17 HTTP/1.1
      Host: {your_Odoo_server_url}

   **Response**: 
   
   .. note:: the report is sent as PDF binary data encoded in `base64 <https://en.wikipedia.org/wiki/Base64>`_, it must be decoded and may need to be saved to disk before use

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {
        'report': [
            {
                'id': 12, 
                'state': 'true',
                'format': 'pdf',
                'result': 'R0lGODlhbgCMAPf\/APbr48VySrxTO7IgKt2qmKQdJeK8lsFjROG5p\
                /nz7Zg3\nMNmnd7Q1MLNVS9GId71hSJMZIuzTu4UtKbeEeakhKMl8U8WYjfr18YQaIbAf\n
                KKwhKdKzqpQtLebFortOOejKrOjZ1Mt7aMNpVbAqLLV7bsNqR+3WwMqEWenN\n
                sZYxL\/Ddy\/Pm2e7ZxLlUQrIjNPXp3bU5MbhENbEtLtqhj5ZQTfHh0bMxL7Ip\n
                NsNyUYkZIrZJPcqGdYIUHb5aPKkeJnoUHd2yiJkiLKYiKLRFOsyJXKVDO8up\n
                osFaS+TBnK4kKti5sNaYg\/z49aqYl5kqLrljUtORfMOlo\/36+H4ZH
                ...
                ...
                ...'
            },
            {
                'id': 17, 
                'state': 'true',
                'format': 'pdf',
                'result': '9iggMd1TLtbRKUdKXEQFsd4XrZRPLIgMZUeJ+jKvrAlK6AhJ65A\nMp
                MpKuC3j5obIsRwS7hAN8l\/YtvDvnYXHbAoLI47SIUsOMenorF4gO\/m4+fH\npo4vLZ8oKMukqp0cJbhVSMV2U
                uPR0bAfMLIrLrg\/OcJwT8h+Vt+wn8eurLlh\nQrIfKHQOHHQOHf\/\/\/\/\/
                \/\/yH5BAEAAP8ALAAAAABuAIwAAAj\/AP8JHDhQXjpz\n\/PopXNiPn0OHDRMmbKhQIsOJFS1SxAhxI
                8SHFzVeDBnx48iNBAeeOkcxokeX\nFRdOnAlSokaaLXNujJkxo8iYHRkKtWkzZ
                SsaOXkAWsoUECynsHgoqEW1q
                ...
                ...
                ...'
            }
        ]
      }
      
   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :reqheader Authorization: The OAuth protocol parameters to authenticate.
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: there’s no resource
   :statuscode 401: authentication failed
   :statuscode 403: if any error raise