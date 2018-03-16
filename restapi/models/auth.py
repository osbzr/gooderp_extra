  # -*- coding: utf-8 -*-
# Part of Odoo. See COPYRIGHT & LICENSE files for full copyright and licensing details.

from odoo import models, api, fields, _
import string
try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse
import urllib
import hmac
import hashlib
import random
import time
from odoo.http import request
from datetime import datetime, timedelta
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as df

class AuthAuth(models.Model):
    _name = 'auth.auth'

    name = fields.Char(string="Name", required=True, help="Your application name")
    description = fields.Text(string="Description", help="Your application description")
    organization_name = fields.Char(string="Organization Name", help="Your application name")
    organization_website = fields.Char(string=" Website", help="Your application name")
    privacy_policy_url = fields.Char(string="Privacy Policy URL", help="The URL for your application or service's privacy policy.")
    terms_service_url = fields.Char(string="Terms of Service URL", help="The URL for your application or service's terms of service. ")
    consumer_key = fields.Char(string="Consumer Key")
    consumer_secret = fields.Char(string="Consumer Secret Key")
    user_id = fields.Many2one("res.users", string='User', required=True)
    active = fields.Boolean("Active", default=True)
    request_token_ids = fields.One2many('auth.request.token', 'auth_id', string="Request Token")
    auth_code_ids = fields.One2many('auth.auth.code', 'auth_id', string="Authorization Code")
    access_token_ids = fields.One2many('auth.access.token', 'auth_id', string="Access Tokens", domain=[('access_token_validity', '>', fields.Datetime.now())])
    access_token = fields.Char(string="Access Token")
    access_token_secret = fields.Char(string="Access Token Secret")
    refresh_token = fields.Char(string="Refresh Token")
    auth_token = fields.Char(string="Auth Token")
    auth_token_validity = fields.Datetime(string="Authorization Token Expire")
    redirect_uris = fields.One2many("redirect.uri", "auth_id" ,string="Redirect URIs")

    _sql_constraints = [
            ('consumer_key_uniq', 
            'unique (consumer_key)', 
            'Consumer Key must be unique!'),]

    used_nonce = {}

    @api.multi
    def name_get(self):
        res = []
        for auth in self:
            res.append((auth.id, auth.name + ' (' + auth.user_id.name + ')'))
        return res

    @api.model
    def create(self, vals):
        """
            Generate Consumer key and Consumer Secret on Create.
        """
        vals['consumer_secret'] = self.generate_token()
        vals['consumer_key'] = self.generate_token()
        return super(AuthAuth, self).create(vals)

    @api.multi
    def generate_refresh(self):
        """
            Generate Refresh Token.
        """
        for rec in self:
            rec.refresh_token = self.generate_token()

    @api.multi
    def revoke_refresh(self):
        """
            Generate Refresh Token.
        """
        for rec in self:
            rec.refresh_token = ''

    @api.multi
    def revoke_access(self):
        """
            Generate Refresh Token.
        """
        for rec in self:
            rec.access_token = ''
            rec.access_token_secret = ''

    @api.multi
    def generate_access(self):
        """
            Generate Access Token.
        """
        for rec in self:
            rec.access_token = self.generate_token()
            rec.access_token_secret = self.generate_token()


    @api.model
    def generate_token(self):
        """
            Combination of 32 Characters in uppercase and lowercase and digits.
        """
        return ''.join(random.choice(string.ascii_uppercase + \
            string.digits + string.ascii_lowercase) for _ in range(32))

    @api.one
    def update_key_secret(self):
        """
            Update Consumer Key & Secret.
        """
        self.consumer_key = self.generate_token()
        self.consumer_secret = self.generate_token()

    @api.model
    def get_authorize_user(self, key):
        """
            Returns Authorized user for given key.
        """
        if key:
            return self.sudo().search([('consumer_key', '=', key)], limit=1)
        return False

    @api.model
    def get_authorize_user_request_token(self, request_token):
        """
            Returns Authorized user for given request_token.
        """
        if request_token:
            return self.sudo().search([('request_token_ids', '=', request_token)], limit=1)
        return False

    @api.model
    def key_validation(self, key):
        """
            Checks whether key is valid or not.
        """
        if key:
            valid = self.sudo().search([('consumer_key', '=', key)], limit=1)
            if valid:
                return True
        return False

    @api.model
    def compare_signature(self, params, method, base_url):
        """
            Compare generated signature with user provided signature.
        """
        oauth_signature = params.get('oauth_signature')
        if oauth_signature:
            del params['oauth_signature']
            generated_signature = self.generate_oauth_signature(
                params, method, base_url)
            if generated_signature and oauth_signature == generated_signature:
                return True
            elif urllib.unquote(oauth_signature).decode('utf8')==generated_signature:
                return True
        return False

    @api.model
    def authentication(self, params, method, base_url):
        """
            Verify that the provided request signature matches our generated signature,
            this ensures the user has a valid key/secret.
        """
        valid = self.key_validation(params.get('oauth_consumer_key'))
        if not valid:
            return False, {'error': {'code': 401, 'message': 'Key Invalid'}}
        timestamp_nonce = self.check_timestamp_auth(params.get('oauth_timestamp'), params.get('oauth_nonce'))
        if not timestamp_nonce:
            return False, {'error': {'code': 401, 'message': 'Invalid Timestamp or Nonce'}}
        same_sig = self.compare_signature(params, method, base_url)
        if not same_sig:
            return False, {'error': {'code': 401, 'message': 'Authentication Required'}}
        return True, False

    @api.model
    def generate_oauth_signature(self, params, method, base_url):
        """
            Generate Signature using HMAC algorithm of key/secret.
        """
        oauth_consumer_secret = None
        if params.get('oauth_consumer_key'):
            user = self.get_authorize_user(params['oauth_consumer_key'])
            oauth_consumer_secret = user.consumer_secret + '&'
            if not user:
                return False
            if params.get('for_access_token'):
                verifier = self.env['auth.request.token'].sudo().search([('request_token', '=', params['oauth_token'])])
                oauth_consumer_secret += verifier.request_token_secret
                del params['for_access_token']
            if params.get('for_request_data'):
                # verifier = self.env['auth.request.token'].sudo().search([('request_token', '=', params['oauth_token'])])
                oauth_consumer_secret += user.access_token_secret
                del params['for_request_data']
        if dict(params).get('oauth_signature_method')=='PLAINTEXT':
            return oauth_consumer_secret          

        parse_url = urlparse.urlparse(base_url)
        scheme = parse_url.scheme
        if request.httprequest.environ.get('HTTP_X_FORWARDED_PROTO') and request.httprequest.environ['HTTP_X_FORWARDED_PROTO'] == 'https':
            scheme = 'https'
        base_url = "%s://%s%s%s" % (
        scheme,
        parse_url.hostname,
        "" if not parse_url.port or {"http":80,"https":443}[parse_url.scheme]\
                == parse_url.port else ":%d" % parse_url.port,
        parse_url.path,)
        base_url = urllib.quote(base_url).replace('+','%20').replace('/', '%2F')
        for key, val in params.items():
            params[key] = urllib.unquote(val)    
        params = self.normalize_params(params)
        query_string = ''
        query_string = params
        base_str = method + '&' + base_url + '&' + query_string
        _hash = hmac.new(oauth_consumer_secret.encode('utf-8') , base_str.encode('utf-8'), hashlib.sha1).digest()

        signature = urllib.quote_plus(_hash.encode('base64').rstrip('\n'))
        return signature

    def normalize_params(self, params):
        """
            Normalize each parameter by assuming each parameter may have already been
            encoded, so attempt to decode, and then re-encode according to RFC 3986.
        """
        def escape(s):
            """Escape a URL including any /."""
            return urllib.quote(s, safe='~')

        def _utf8_str(s):
            """Convert unicode to utf-8."""
            if isinstance(s, unicode):
                return s.encode("utf-8")
            else:
                return str(s)
        try:
            # Exclude the signature if it exists.
            del params['oauth_signature']
        except:
            pass
        # Escape key values before sorting.
        key_values = [(escape(_utf8_str(k)), escape(_utf8_str(v))) \
            for k,v in params.items()]
        # Sort lexicographically, first after key, then after value.
        key_values.sort()
        # Combine key value pairs into a string.
        return escape('&'.join(['%s=%s' % (k, v) for k, v in key_values]))

    @api.model
    def check_timestamp_auth(self, timestamp, nonce):
        """
            Verify that the timestamp and nonce provided with the request are valid. This prevents replay attacks where
            an attacker could attempt to re-send an intercepted request at a later time.
            A timestamp is valid if it is within 15 minutes of now.
            A nonce is valid if it has not been used within the last 15 minutes.
        """
        valid_window = 15 * 60;
        if float(timestamp) < time.time() - valid_window or float(timestamp) > time.time() + valid_window:
            return False
        for n, t in self.used_nonce.items():
            if float(t) < time.time() - valid_window or float(timestamp) > time.time() + valid_window:
                del self.used_nonce[n]
        if nonce in self.used_nonce.keys():
            return False
        self.used_nonce.update({nonce: timestamp})
        return True
        
class RedirectUri(models.Model):
    _name = 'redirect.uri'

    url = fields.Char(string="Url")
    auth_id = fields.Many2one("auth.auth", string="Auth")

class AuthAuthCode(models.Model):
    _name = 'auth.auth.code'
    _rec_name = 'auth_code'

    auth_code = fields.Char(string="Auth Code")
    used = fields.Boolean('Used', default=False)
    auth_id = fields.Many2one('auth.auth', 'Auth')

class AuthAuthCode(models.Model):
    _name = 'auth.access.token'
    _rec_name = 'access_token'

    access_token = fields.Char(string="Auth Token")
    access_token_validity = fields.Datetime('Access Token Validity')
    auth_id = fields.Many2one('auth.auth', 'Auth')

    @api.multi
    def revoke_access(self):
        """
            Generate Refresh Token.
        """
        self.unlink()

    @api.multi
    def access_token_cron(self):
        check_datetime = datetime.now()-timedelta(days=3)
        self.env['auth.access.token'].search([('access_token_validity', '<', check_datetime.strftime(df))]).unlink()

class AuthRequestToken(models.Model):
    _name = 'auth.request.token'
    _rec_name = 'request_token'

    request_token = fields.Char(string="Request Token")
    token_verifier = fields.Char(string="Verifier")
    request_token_secret = fields.Char(string="Request Token Secret")
    request_token_validity = fields.Datetime('Request Token Validity')
    auth_id = fields.Many2one('auth.auth', 'Auth')
    callback_uri = fields.Char(string="Callback Uri")

    @api.model
    def get_request_token(self, request_token, auth=False):
        """
            Returns Request Token record for given request_token.
        """
        dom = [('request_token', '=', request_token)]
        if auth:
            dom.append(('auth_id', '=', auth.id))
        if request_token:
            return self.sudo().search(dom, limit=1)
        return False

    @api.model
    def generate_verifier(self):
        """
            Combination of 32 Characters in uppercase and lowercase and digits.
        """
        return ''.join(random.choice(string.digits) for _ in range(7))

    @api.multi
    def is_valid_varifier(self, verifier):
        return

    @api.model
    def is_valid_request(self, request_token, verifier, auth=False):
        """
            Validates, whether request token and verifiet is valid.
        """
        return self.sudo().search([('request_token', '=', request_token), ('auth_id', '=', auth.id), ('token_verifier', '=', verifier)])

    @api.multi
    def request_token_cron(self):
        check_datetime = datetime.now()-timedelta(days=3)
        self.env['auth.request.token'].search([('request_token_validity', '<', check_datetime.strftime(df))]).unlink()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: