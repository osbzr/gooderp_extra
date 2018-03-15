# -*- coding: utf-8 -*-
# Copyright 2014 wangbuke <wangbuke@gmail.com>
# Copyright 2017 Jarvis <jarvis@odoomod.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import api, models, tools


class IrMailServer(models.Model):
    _inherit = "ir.mail_server"

    @api.model
    def send_email(self, message, mail_server_id=None, smtp_server=None, smtp_port=None,
                   smtp_user=None, smtp_password=None, smtp_encryption=None, smtp_debug=False):
        # Get SMTP Server Details from Mail Server
        mail_server = None
        if mail_server_id:
            mail_server = self.sudo().browse(mail_server_id)
        elif not smtp_server:
            mail_server = self.sudo().search([], order='sequence', limit=1)

        if mail_server:
            smtp_user = mail_server.smtp_user
        else:
            # we were passed an explicit smtp_server or nothing at all
            smtp_user = smtp_user or tools.config.get('smtp_user')

        # Replace Header
        message.replace_header('From', '%s <%s>' % (message['From'], smtp_user))
        if message.has_key('return-path'):
            message.replace_header('return-path', '%s' % (smtp_user,))
        else:
            message.add_header('return-path', '%s' % (smtp_user,))

        return super(IrMailServer, self).send_email(message, mail_server_id, smtp_server, smtp_port,
                                                    smtp_user, smtp_password, smtp_encryption, smtp_debug)
