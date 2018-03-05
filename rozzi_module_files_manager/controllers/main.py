# -*- coding: utf-8 -*-

from openerp import http
from openerp.http import request
from openerp.tools import misc
from openerp.addons.web.controllers.main import serialize_exception,content_disposition

import base64
import os


import json

class Home(http.Controller):

    @http.route(['/rozzi_module_files_manager/get_file_list'],type='http',auth='user')
    def get_file_list(self,*args,**kargs):
        m= kargs['m']

        #src=misc.file_open('rozzi_module_files_manager').name
        #dirname= misc.file_open('rozzi_module_files_manager/__init__.py').name
        print m
        src=misc.file_open(m+'\\__init__.py').name
        print src
        addons_path= os.path.dirname(os.path.dirname(src))
        dirname=addons_path+'\\'+m+'\\'
        
        print dirname
        result = []
        for maindir, subdir, file_name_list in os.walk(dirname):
            print 'maindir=========='
            print maindir
            print 'subdir=========='
            print subdir
            print 'file_name_list=========='
            print file_name_list
            
            for filename in file_name_list:
                print 'filename=========='+filename
                
                if filename.find('.pyc')>-1:
                    pass
                else:    
                    
                    apath = os.path.join(maindir, filename)
                    apath = apath.replace(dirname,'')

                    result.append(apath)
        print result
        ret={
            'files':result
        }        
        return json.dumps(ret)
        

    @http.route(['/rozzi_module_files_manager/read_file'],type='http',auth='user')
    def read_file(self,*args,**kargs):
        m= kargs['m']
        f= kargs['f']

        src=misc.file_open(m+'\\'+f).name
        
        with open(src, 'r') as input_stream:
                filecontent = input_stream.read()

        ret={
            'data':filecontent
        }        
        return json.dumps(ret)
        
    
    @http.route(['/rozzi_module_files_manager/save_file'],type='http',auth='user', csrf=False) #, methods=['POST']
    def save_file(self,*args,**kargs):
        m= kargs['m']
        f= kargs['f']
        data= kargs['data']
        

        src=misc.file_open(m+'\\'+f).name
        
        fileobj=file(src,'w+')
        try:

            fileobj.write(data)

        except Exception:
            raise Exception

        finally:
            fileobj.close()

        # your treatment
        return 'save completed'
        