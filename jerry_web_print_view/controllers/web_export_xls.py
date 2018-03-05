# -*- coding: utf-8 -*-

try:
    import json
except ImportError:
    import simplejson as json

import odoo.http as http
from odoo.http import request
from odoo.addons.web.controllers.main import ExcelExport

import logging
logger = logging.getLogger(__name__)

class ExcelExportView(ExcelExport):
    def __getattribute__(self, name):
        if name == 'fmt':
            raise AttributeError()
        return super(ExcelExportView, self).__getattribute__(name)

    @http.route('/web/export/xls_view', type='http', auth='user')
    def export_xls_view(self, data, token):
        logger.info('+++ begin export_xls_view ++++')
        logger.info(data)
        logger.info(token)
        data = json.loads(data)
        model = data.get('model', [])
        columns_headers = data.get('headers', [])
        rows = data.get('rows', [])
        logger.info(rows)
        logger.info('+++ end export_xls_view ++++')
        return request.make_response(
            self.from_data(columns_headers, rows),
            headers=[
                ('Content-Disposition', 'attachment; filename="%s"'
                 % self.filename(model)),
                ('Content-Type', self.content_type)
            ],
            cookies={'fileToken': token}
        )
