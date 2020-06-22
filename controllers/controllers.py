# -*- coding: utf-8 -*-
# from odoo import http


# class Formations(http.Controller):
#     @http.route('/formations/formations/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/formations/formations/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('formations.listing', {
#             'root': '/formations/formations',
#             'objects': http.request.env['formations.formations'].search([]),
#         })

#     @http.route('/formations/formations/objects/<model("formations.formations"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('formations.object', {
#             'object': obj
#         })
