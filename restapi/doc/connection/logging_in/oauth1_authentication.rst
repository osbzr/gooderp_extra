OAuth1 Authentication
=====================

Start with setting up a new consumer by following the instructions on :ref:`configuration`. When you have obtained a ``key`` and a ``secret`` you can try out OAuth 1.0 ``resapi/1.0/common/oauth1`` flow goes as follows to get authorized:

.. note:: **OAuth endpoints:**

    1. :ref:`POST {your_Odoo_server_url}/restapi/1.0/common/oauth1/request_token <oauth1-request-token>` (Temporary Credential Request endpoint)
    2. :ref:`GET {your_Odoo_server_url}/restapi/1.0/common/oauth1/authorize <oauth1-authorize>` (Resource Owner Authorization endpoint)
    3. :ref:`POST {your_Odoo_server_url}/restapi/1.0/common/oauth1/access_token <oauth1-access-token>` (Token Credentials Request endpoint)

.. _oauth1-request-token:

1. Temporary Credential Request
-------------------------------

Obtain a request token which will identify you (the consumer) in the next step. At this stage you will only need your consumer key and secret.

.. http:post:: /restapi/1.0/common/oauth1/request_token

   **Request**:

   .. sourcecode:: http

      POST /restapi/1.0/common/oauth1/request_token HTTP/1.1
      Host: {your_Odoo_server_url}
      Authorization: OAuth oauth_consumer_key='uwCrAHAQbL7D9cvJLIztNaZ0bziEGMDh', 
                           oauth_nonce='71257790252100875101500704380', 
                           oauth_callback='https%3A%2F%2F127.0.0.1%2Fcallback', 
                           oauth_signature_method='HMAC-SHA1', 
                           oauth_timestamp='1500704388', 
                           oauth_signature='KbLt0XDVjljXhMJHmmpWxHkFnfs%3D', 
                           oauth_version='1.0'

   **Response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {
        'oauth_token': 'mXYKtuv8k3NJfnpLMpU3KFuEijXx2Aat',
        'oauth_token_secret': 'QAlvAmzyULWeitpe24oNhj3n91los7W5'
      }

   :query oauth_consumer_key: Odoo ``consumer key``
   :query oauth_nonce: A randomly selected value provided by your application, which is unique for each authorization request. During the OAuth callback phase, your application must check that this value matches the one you provided during authorization. This mechanism is important for the security of your application.
   :query oauth_callback: An absolute URL to which the Odoo will redirect the User back when the Obtaining User Authorization step is completed.
   :query oauth_signature_method: The signature method that Consumer used to sign the request. The protocol defines three signature methods: ``HMAC-SHA1``, ``RSA-SHA1``, and ``PLAINTEXT``.
   :query oauth_timestamp: The timestamp is expressed in the number of seconds since January 1, 1970 00:00:00 GMT. The timestamp value MUST be a positive integer and MUST be equal or greater than the timestamp used in previous requests.
   :query oauth_singature: Base64-encoded HMAC-SHA256 signature signed with the consumer's private key containing the all the components of the request and some OAuth value. The signature can be used to verify that the identity URL wasn’t modified because it was sent by the server.
   :query oauth_version: OPTIONAL. If present, value MUST be 1.0. Odoo assume the protocol version to be 1.0 if this parameter is not present. Odoo's response to non-1.0 value is left undefined.
   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :reqheader Authorization: The OAuth protocol parameters to authenticate.
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: there's no resource
   :statuscode 401: authentication failed

.. _oauth1-authorize:

2. Resource Owner Authorization
-------------------------------

Obtain authorization from the user (resource owner) to access their protected resources (customers, orders, etc.). This is commonly done by redirecting the user to a specific url to which you add the request token as a query parameter. Note that not all services will give you a verifier even if they should. Also the oauth_token given here will be the same as the one in the previous step.

.. http:get:: /restapi/1.0/common/oauth1/authorize

   **Request**:

   .. sourcecode:: http

      GET /restapi/1.0/common/oauth1/authorize HTTP/1.1
      Host: {your_Odoo_server_url}

   **Response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

      { 
        'oauth_token': 'mXYKtuv8k3NJfnpLMpU3KFuEijXx2Aat',
        'oauth_verifier': 'sdflk3450FASDLJasd2349dfs'
      }

   :query oauth_token: OPTIONAL. The Request Token obtained in the previous step.
   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :reqheader Authorization: OPTIONAL OAuth token to authenticate
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: there's no resource
   :statuscode 401: authentication failed

.. _oauth1-access-token:

3. Token Credentials Request
----------------------------

Obtain an access token from the Odoo. Save this token as it can be re-used later. In this step we will re-use most of the credentials obtained uptil this point.

.. http:post:: /restapi/1.0/common/oauth1/access_token

   **Request**:

   .. sourcecode:: http

      POST /restapi/1.0/common/oauth1/access_token HTTP/1.1
      Host: {your_Odoo_server_url}
      Authorization: OAuth oauth_consumer_key='uwCrAHAQbL7D9cvJLIztNaZ0bziEGMDh', 
                           oauth_token='mXYKtuv8k3NJfnpLMpU3KFuEijXx2Aat', 
                           oauth_nonce='156754554473268986001500738176', 
                           oauth_signature_method='HMAC-SHA1', 
                           oauth_timestamp='1500738189',
                           oauth_verifier='sdflk3450FASDLJasd2349dfs', 
                           oauth_signature='KbLt0XDVjljXhMJHmmpWxHkFnfs%3D', 
                           oauth_version='1.0' 

   **Response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {
        'oauth_token': 'RF7gImCv0B58eogLiPmOmNPizZEVVUWP',
        'oauth_token_secret': 'oxBUTIjTl8gfbxEv2jpXo5rRtQ16u3Lg'
      }

   :query oauth_consumer_key: Odoo ``consumer key``
   :query oauth_token: The Request Token obtained previously.
   :query oauth_nonce: A randomly selected value provided by your application, which is unique for each authorization request. During the OAuth callback phase, your application must check that this value matches the one you provided during authorization. This mechanism is important for the security of your application.
   :query oauth_signature_method: The signature method that Consumer used to sign the request. The protocol defines three signature methods: ``HMAC-SHA1``, ``RSA-SHA1``, and ``PLAINTEXT``.
   :query oauth_timestamp: The timestamp is expressed in the number of seconds since January 1, 1970 00:00:00 GMT. The timestamp value MUST be a positive integer and MUST be equal or greater than the timestamp used in previous requests.
   :query oauth_verifier: The verification code received from the Odoo.
   :query oauth_singature: Base64-encoded HMAC-SHA256 signature signed with the consumer's private key containing the all the components of the request and some OAuth value. The signature can be used to verify that the identity URL wasn’t modified because it was sent by the server.
   :query oauth_version: OPTIONAL. If present, value MUST be 1.0. Odoo assume the protocol version to be 1.0 if this parameter is not present. Odoo's response to non-1.0 value is left undefined.
   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :reqheader Authorization: The OAuth protocol parameters to authenticate
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: there's no resource
   :statuscode 401: authentication failed