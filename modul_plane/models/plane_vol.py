from odoo import models, fields
class plane_vol(models.Model):
    _name = 'plane.vol'
    codi = fields.Integer('Codi', required = True)
    passatgers = fields.Integer('Passatgers')
    datasortida = fields.Date('Data Sortida')
    dataarrivada = fields.Date('Data Arrivada')