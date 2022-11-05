from odoo import models, fields, api


class VehicleDetails(models.Model):
    _name = 'vehicle.details'
    _description = 'Vehicle Management Details'
     
    reg_number = fields.Char('Reg Number', required=True)
    owner_name = fields.Char('Owner name', required=True)
    owner_mobile = fields.Char('Owner Mobile Number', required=True)
    owner_nic = fields.Char('Owner NIC number', required=True)
    nic_image = fields.Binary('NIC Image', required=True)
    insurance_number = fields.Char('Insurance Number')
    insurance_image = fields.Binary('Insurance Image', required=True)
    revenue_license_number = fields.Char('Revenue License number')
    revenue_license_image = fields.Binary('Revenue License Image', required=True)
    insurance_next_expire_date = fields.Date('Insurance next expire date')
    Revenue_license_next_expire_date = fields.Date('Revenue License Next expire date')
    availability = fields.Selection([
        ('1', 'Yes'),
        ('0', 'No')
    ], string='Availability')