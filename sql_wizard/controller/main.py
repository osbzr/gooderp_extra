# -*- coding: utf-8 -*-
from odoo import http
class ParseSQL(http.Controller):

    @http.route('/sql', auth='user')
    def handler(self):
        return '''
  First name: <input type="text" name="fname" />
  Last name: <input type="text" name="lname" />
  <input type="submit" value="Submit" />
  '''