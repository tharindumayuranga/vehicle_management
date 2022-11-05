from odoo import models, fields, api


class DriverDetails(models.Model):
    _name = 'driver.details'
    _description = 'Vehicle Management Driver Details'
     
    full_name = fields.Char('Driver Full Name', required=True)
    address = fields.Char('Permanent Address', required=True)
    age = fields.Integer('Driver Age')
    nic = fields.Char('Driver NIC number', required=True)
    nic_image = fields.Binary('Driver NIC Image', required=True)
    license_number = fields.Char('Driver Valid Driving license number', required=True)
    driving_license_image = fields.Binary('Driving License Image', required=True)
    license_expire_date = fields.Date('Drive License Expire Date')