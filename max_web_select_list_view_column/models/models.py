# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Setting(models.Model):
    _name = 'max.web.select.list.view.column.setting'

    name = fields.Char()
    res_model = fields.Char()
    user_id = fields.Many2one(comodel_name='res.users', ondelete='cascade')
    xml_id = fields.Char()
    columns = fields.Char()

    @api.model
    def get_columns(self, args, vals):
        name = vals.get('name', '')
        res_model = vals.get('res_model', '')
        user_id = vals.get('user_id', 0)
        xml_id = vals.get('xml_id', '')
        settings = self.env['max.web.select.list.view.column.setting']
        records = settings.search([('name', '=', name),
                                   ('res_model', '=', res_model),
                                   ('user_id', '=', user_id),
                                   ('xml_id', '=', xml_id)])
        if records:
            return records[0].columns.split(',')

        return []

    @api.model
    def save_columns(self, args, vals, columns):
        name = vals.get('name', '')
        res_model = vals.get('res_model', '')
        user_id = vals.get('user_id', 0)
        xml_id = vals.get('xml_id', '')

        settings = self.env['max.web.select.list.view.column.setting']
        records = settings.search([('name', '=', name),
                                   ('res_model', '=', res_model),
                                   ('user_id', '=', user_id),
                                   ('xml_id', '=', xml_id)])
        if records:
            records[0].columns = ','.join(columns)
        else:
            settings.create({
                'name': name,
                'res_model': res_model,
                'user_id': user_id,
                'xml_id': xml_id,
                'columns': ','.join(columns),
            })

        return True

    @api.model
    def reset_columns(self, args, vals):
        name = vals.get('name', '')
        res_model = vals.get('res_model', '')
        user_id = vals.get('user_id', 0)
        xml_id = vals.get('xml_id', '')

        self.env['max.web.select.list.view.column.setting']\
            .search([('name', '=', name),
                     ('res_model', '=', res_model),
                     ('user_id', '=', user_id),
                     ('xml_id', '=', xml_id)]).unlink()
        return True


