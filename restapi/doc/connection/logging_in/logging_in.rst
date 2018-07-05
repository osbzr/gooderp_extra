Logging In
==========

Odoo requires users of the REST API to be authenticated before they can query most data.

The ``restapi/1.0/common`` endpoint provides meta-calls which don't require authentication, such as the authentication itself or fetching version information. To verify if the connection information is correct before trying to authenticate, the simplest call is to ask for the server's version through the ``restapi/1.0/common/version`` endpoint. The authentication itself is done through the **OAuth 1.0** ``restapi/1.0/common/oauth1`` or **OAuth 2.0** ``restapi/1.0/common/oauth2`` endpoints.

How you can do
--------------

.. toctree::
   :maxdepth: 2

   version_info
   oauth1_authentication
   oauth2_authentication