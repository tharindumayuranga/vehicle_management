# -*- coding: utf-8 -*-
# from odoo import http


# class VehicleManagement(http.Controller):
#     @http.route('/vehicle_management/vehicle_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vehicle_management/vehicle_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vehicle_management.listing', {
#             'root': '/vehicle_management/vehicle_management',
#             'objects': http.request.env['vehicle_management.vehicle_management'].search([]),
#         })

#     @http.route('/vehicle_management/vehicle_management/objects/<model("vehicle_management.vehicle_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vehicle_management.object', {
#             'object': obj
#         })
