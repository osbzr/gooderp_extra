OAuth2 Authentication
======================

Setup credentials following the instructions on :ref:`configuration`. When you have obtained a ``client_id`` and a ``client_secret`` you can try out OAuth 2.0 ``resapi/1.0/common/oauth2`` flow goes as follows to get authorized:

.. note:: **OAuth endpoints:**

    1. :ref:`GET {your_Odoo_server_url}/restapi/1.0/common/oauth2/authorize <oauth2-authorize>` (Resource Owner Authorization endpoint)
    2. :ref:`POST {your_Odoo_server_url}/restapi/1.0/common/oauth2/access_token <oauth2-access-token>` (Token Credentials Request endpoint)
    
.. _oauth2-authorize:

1. Resource Owner Authorization
-------------------------------

User authorization through redirection. First we will create an authorization url from the base URL given by the Odoo and the credentials previously obtained.

.. http:get:: /restapi/1.0/common/oauth2/authorize

   **Request**:

   .. sourcecode:: http

      GET /restapi/1.0/common/oauth2/authorize HTTP/1.1
      Host: {your_Odoo_server_url}
      Authorization: OAuth client_id='uwCrAHAQbL7D9cvJLIztNaZ0bziEGMDh', 
                           state='Y1Ux1iNPvn6KYQK5Lj84WJ9VJrQw1L', 
                           redirect_uri='https%3A%2F%2F127.0.0.1%2Fcallback', 
                           response_type='code'

   **Response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

      { 
        'code': 'dcee1806d2c50d0fb598',
        'state': 'Y1Ux1iNPvn6KYQK5Lj84WJ9VJrQw1L'
      }

   :query client_id: Odoo ``consumer key``
   :query state: Specifies any additional URL-encoded state data to be returned in the callback URL after approval.
   :query redirect_uri: An absolute URL to which the Odoo will redirect the User back when the obtaining User Authorization step is completed.
   :query response_type: Must be ``code`` for this authentication flow.
   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :reqheader Authorization: The OAuth protocol parameters to authenticate.
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: there’s no resource
   :statuscode 401: authentication failed

.. _oauth2-access-token:

2. Token Credentials Request
----------------------------

Fetch an access token from the Odoo using the authorization code obtained during user authorization.

.. http:post:: /restapi/1.0/common/oauth2/access_token

   **Request**:

   .. sourcecode:: http

      POST /restapi/1.0/common/oauth2/access_token HTTP/1.1
      Host: {your_Odoo_server_url}
      Authorization: OAuth client_id='uwCrAHAQbL7D9cvJLIztNaZ0bziEGMDh', 
                           client_secret='FtHzOQVEs0aSEL9AXuIe9k7X6E2MekU7', 
                           redirect_uri='https%3A%2F%2F127.0.0.1%2Fcallback', 
                           code='dcee1806d2c50d0fb598'
                           grant_type='authorization_code'

   **Response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

      { 
        'access_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIn',
        'token_type': 'bearer',
        'access_token_validity': '7/20/2017 12:00:05',
        'refresh_token': 'ZXIiLCJnaXZlbl9uYW1lIjoiRnJhbmsifQ' 
      }

   :query client_id: Odoo ``consumer key``
   :query client_secret: Odoo ``consumer secret``
   :query redirect_uri: An absolute URL to which the Odoo will redirect the User back when the obtaining User Authorization step is completed.
   :query code: Authorization code the consumer must use to obtain the access and refresh tokens.
   :query grant_type: Value must be ``authorization_code`` for this flow.
   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :reqheader Authorization: The OAuth protocol parameters to authenticate.
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: there’s no resource
   :statuscode 401: authentication failed