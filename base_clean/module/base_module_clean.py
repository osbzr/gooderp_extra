# -*- coding: utf-8 -*-
# Copyright 2017 Jarvis (www.odoomod.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class BaseModuleClean(models.TransientModel):
    _name = "base.module.clean"
    _description = "Clean Module"

    cleaned = fields.Integer('Number of modules cleaned', readonly=True)
    state = fields.Selection([('init', 'init'), ('done', 'done')], 'Status', readonly=True, default='init')
    uninstall_self = fields.Boolean('Uninstall self')

    @api.multi
    def clean_module(self):
        clean_list = self.env['ir.module.module'].search([('create_uid', '!=', None), ('state', '=', 'uninstalled')])
        clean_list.unlink()
        self.write({'cleaned': len(clean_list), 'state': 'done'})

        if self.uninstall_self:
            this = self.env['ir.module.module'].search([('name', '=', 'base_clean')])
            if this.id:
                this.button_immediate_uninstall()

        return False

    @api.multi
    def action_module_open(self):
        res = {
            'domain': str([]),
            'name': 'Modules',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'ir.module.module',
            'view_id': False,
            'type': 'ir.actions.act_window',
        }
        return res
