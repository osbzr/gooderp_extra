# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
try:
    import json
except ImportError:
    import simplejson as json
from types import NoneType
from openerp import api, fields, models, _
import datetime
import xlrd
from openerp.tools import misc
import base64
import os
import tempfile
import random
from openerp import http
from openerp.http import request
from cStringIO import StringIO

import re
try:
    import xlwt
except ImportError:
    xlwt = None


import logging
logger = logging.getLogger(__name__)



class sql_wizard(models.TransientModel):
    _name = "sql.wizard"
    _description = "sql_wizard"

    @api.one
    def calc_sql(self):
        self.env.cr.execute(self.sql)

        if self.sql.find("select") > -1:
            result = self.env.cr.dictfetchall()
            Fstr = '<table border=1>'

            if result[0]:
                keys=result[0].keys()
                Fstr += '<tr style="background-color: rgb(198, 198, 198);">'
                Fstr += '<td ><b>ID</b></td>'
                for key in keys:
                    if key!="id":
                          Fstr += '<td ><b>' + key + '</b></td>'
                Fstr += '</tr>'

            for line in result:
                Fstr += '<tr>'
                Fstr += '<td>' + str(line["id"]) + '</td>'
                for key in keys:
                    if key!="id":
                        if isinstance(line[key], int):
                            Fstr += '<td>' + str(line[key]) + '</td>'

                        elif isinstance(line[key], NoneType):
                            Fstr += '<td>' + '</td>'

                        else:
                            Fstr += '<td>' + line[key] + '</td>'

                Fstr += '</tr>'
            Fstr += '</table>'
            self.res = Fstr
            #self.write({'res': Fstr})

    sql=fields.Text("SQL",default="select * from sql_wizard")
    res=fields.Html("查询结果",computer=calc_sql,store=True)

    @api.multi
    def do_query(self):
        self.calc_sql()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'sql.wizard',
            'view_mode': 'form',
            'view_type': 'form',
            'views': [(False, 'form')],
            'target': 'current',
            'res_id': self.id,
             }
