# -*- coding: utf-8 -*-
from odoo import http

# class MethodContractTotal(http.Controller):
#     @http.route('/method_contract_total/method_contract_total/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_contract_total/method_contract_total/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_contract_total.listing', {
#             'root': '/method_contract_total/method_contract_total',
#             'objects': http.request.env['method_contract_total.method_contract_total'].search([]),
#         })

#     @http.route('/method_contract_total/method_contract_total/objects/<model("method_contract_total.method_contract_total"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_contract_total.object', {
#             'object': obj
#         })