# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models,tools
from odoo.exceptions import UserError
import itertools

class model_empty(models.TransientModel):
    _name='rozzi.empty'
    name= fields.Char(u"名称")


class ir_values(models.Model):
    _inherit = 'ir.values'

    

    @api.model
    @tools.ormcache_context('self._uid', 'action_slot', 'model', 'res_id', keys=('lang',))
    def get_actions(self, action_slot, model, res_id=False):
     
        res=super(ir_values, self).get_actions( action_slot, model, res_id)

        #如果是'rozzi.empty'，直接返回,防死循环
        if model!='rozzi.empty':
            if self.env['res.users'].has_group('rozzi_batch_edit.group_batch_edit_user'):  
                if action_slot=='client_action_multi':
           
                    ir_values_obj = self.env['ir.values']
                    resaction = ir_values_obj.get_actions('client_action_multi', 'rozzi.empty')


                    res=res+ resaction


        return res
        


class rozzi_batch_edit_wizard(models.TransientModel):
    """rozzi_batch_edit"""
    _name = "rozzi.batch.edit.wizard"

    @api.multi
    def confirm(self):
        if self.field_name:
            ids=self.lines.replace('[','').replace(']','').split(',')
            #for id in  range(len(ids)):
            #    ids[id]=int(ids[id])
            ids=[int(i) for i in ids]

            if  self.ttype in ['selection']:
                #
                self.env[self.name].browse(ids).write({self.field_name.name: self.set_value_selection.key});

            elif  self.ttype in ['many2one']:

                self.env[self.name].browse(ids).write({self.field_name.name: int(self.set_value_many2one.key)});

            elif self.ttype in ['date','datetime']:
                self.env[self.name].browse(ids).write({self.field_name.name: self.set_value_datetime});
            elif self.ttype in ['boolean']:
                self.env[self.name].browse(ids).write({self.field_name.name: self.set_value_bool});

            else:
                self.env[self.name].browse(ids).write({self.field_name.name: self.set_value});



        return {'type': 'ir.actions.act_window_close'}


    @api.model
    def default_get(self, fields):
        
 
        context = self._context or {}
        if  not context['active_ids']:
            raise UserError('最少选择一条记录')


        res = super(rozzi_batch_edit_wizard, self).default_get(fields)

        active_model=context['active_model']
        res['name']=active_model
        res['lines'] = context['active_ids']


        return res


    
    name= fields.Char(u"模块名", required=True)
    field_name = fields.Many2one("ir.model.fields", u"字段名")


        
    lines= fields.Char("选中记录", required=True)

    ttype=fields.Selection(related="field_name.ttype",string=u'字段类型')

    set_value= fields.Char(u"修改值")
    set_value_selection= fields.Many2one('rozzi.batch.edit.wizard.selection',u"修改选项")
    set_value_many2one= fields.Many2one('rozzi.batch.edit.wizard.many2one',u"修改关联")
    set_value_datetime= fields.Datetime(u"修改日期")
    set_value_bool= fields.Boolean(u"修改布尔值")

    
    _defaults = {

    }


    #@api.onchange('field_name')
    #def onchange_type(self):
    #    if self.field_name > '':
            

class rozzi_batch_edit_many2one(models.TransientModel):
        """rozzi_batch_edit_fields"""
        _name = "rozzi.batch.edit.wizard.many2one"

        name = fields.Char(u"字段值", required=True)
        key = fields.Char(u"字段索引", required=True)
        field_name = fields.Char(u"字段名", required=True)
        model_name = fields.Char(u"模块名")

        _defaults = {

        }

        @api.model
        def name_search(self, name, args=None, operator='ilike', limit=100):
            context = self._context or {}
            args = args or []
            print context['model']
            print context['field_name']

            # print self.env.active_model

            field_name=self.env['ir.model.fields'].browse([context['field_name']])[0].name
            model=self.env['ir.model.fields'].browse([context['field_name']])[0].relation
            print field_name
            recs = self.env[model].search([('name', operator, name)] , limit=limit)
                #+ args
            name_gets=recs.name_get()
            for name_get in name_gets:
                val={'name':name_get[1],
                     'key':name_get[0],
                     'model_name':context['model'],
                     'field_name': context['field_name']
                     }
                if  self.search_count([('name','=',name_get[1]),('key','=',name_get[0]),('model_name','=',context['model']),('field_name','=',context['field_name'])])==0:
                    self.create(val)

            recs = self.search([('name', operator, name),('model_name','=',context['model']),('field_name','=',context['field_name'])] , limit=limit)
            return recs.name_get()

class rozzi_batch_edit_selection(models.TransientModel):
        """rozzi_batch_edit_fields"""
        _name = "rozzi.batch.edit.wizard.selection"

        name = fields.Char(u"字段名", required=True)
        key = fields.Char(u"字段索引", required=True)
        field_name = fields.Char(u"字段名", required=True)
        model_name = fields.Char(u"模块名")

        _defaults = {

        }

        @api.model
        def name_search(self, name, args=None, operator='ilike', limit=100):
            context = self._context or {}

            print context['model']
            print context['field_name']
            # print self.env.active_model

            field_name = self.env['ir.model.fields'].browse([context['field_name']])[0].name
            print field_name

            fields = [
                field_name
            ]

            ref_fields = self.env[context['model']].fields_get(fields)

            name_gets = ref_fields[field_name]['selection']

            for name_get in name_gets:
                val = {'name': name_get[1],
                       'key': name_get[0],
                       'model_name': context['model'],
                       'field_name': context['field_name']
                       }
                if self.search_count(
                        [('name', '=', name_get[1]), ('key', '=', name_get[0]), ('model_name', '=', context['model']),
                         ('field_name', '=', context['field_name'])]) == 0:
                    self.create(val)

            recs = self.search([('name', operator, name),('model_name','=',context['model']),('field_name','=',context['field_name'])], limit=limit)
            return recs.name_get()