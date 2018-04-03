# -*- coding: utf-8 -*-

from odoo.http import Controller, request, route

from ..tools import make_response, eval_request_params


class RestApi(Controller):
    """
    /api/auth                   POST    - Login in Odoo and set cookies

    /api/<model>                GET     - Read all (with optional domain, fields, offset, limit, order)
    /api/<model>/<id>           GET     - Read one (with optional fields)
    /api/<model>                POST    - Create one
    /api/<model>/<id>           PUT     - Update one
    /api/<model>/<id>           DELETE  - Delete one
    /api/<model>/<id>/<method>  PUT     - Call method (with optional parameters)
    """

    @route('/api/auth', auth='none', methods=["POST"])
    @make_response()
    def authenticate(self, db, login, password):
        # Before calling /api/auth, call /web?db=*** otherwise web service is not found
        print "1"
        request.session.authenticate(db, login, password)
        return request.env['ir.http'].session_info()

    @route('/api/<string:model>', auth='user', methods=["GET"])
    @make_response()
    def search_read(self, model, **kwargs):
        print "2"
        eval_request_params(kwargs)
        return request.env[model].search_read(**kwargs)

    @route('/api/<string:model>/<int:id>', auth='user', methods=["GET"])
    @make_response()
    def read(self, model, id, **kwargs):
        print "3"
        eval_request_params(kwargs)
        result = request.env[model].browse(id).read(**kwargs)
        return result and result[0] or {}

    @route('/api/<string:model>', auth='user',
           methods=["POST"], csrf=False)
    @make_response()
    def create(self, model, **kwargs):
        print "4"
        eval_request_params(kwargs)
        return request.env[model].create(**kwargs).id

    @route('/api/<string:model>/<int:id>', auth='user',
           methods=["PUT"], csrf=False)
    @make_response()
    def write(self, model, id, **kwargs):
        print "5"
        eval_request_params(kwargs)
        return request.env[model].browse(id).write(**kwargs)

    @route('/api/<string:model>/<int:id>', auth='user',
           methods=["DELETE"], csrf=False)
    @make_response()
    def unlink(self, model, id):
        print "6"
        return request.env[model].browse(id).unlink()

    @route('/api/<string:model>/<int:id>/<string:method>', auth='user',
           methods=["PUT"], csrf=False)
    @make_response()
    def custom_method(self, model, id, method, **kwargs):
        print "7"
        eval_request_params(kwargs)
        record = request.env[model].browse(id)
        return getattr(record, method)(**kwargs)
