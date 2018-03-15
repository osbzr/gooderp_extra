# -*- coding: utf-8 -*-
# Copyright 2017 Jarvis (www.odoomk.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class Import(models.TransientModel):
    _inherit = 'base_import.import'

    @api.multi
    def do(self, fields, options, dryrun=False):
        self.ensure_one()
        if dryrun:
            return super(Import, self).do(fields, options, dryrun)
        else:
            try:
                data, import_fields = self._convert_import_data(fields, options)
                data = self._parse_import_data(data, import_fields, options)
            except ValueError, error:
                return [{
                    'type': 'error',
                    'message': unicode(error),
                    'record': False,
                }]

            model = self.env[self.res_model].with_context(import_file=True)
            for d in data:
                _logger.info('importing %s', d)
                import_result = model.load(import_fields, [d])
                self._cr.commit()

            _logger.info('done')
            return import_result['messages']
