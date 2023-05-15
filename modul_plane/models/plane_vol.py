from odoo import models, fields
class plane_vol(models.Model):
    _name = 'plane.vol'
    passatgers = fields.Integer('Passatgers')
    datasortida = fields.DateTime('Data Sortida')
    dataarrivada = fields.DateTime('Data Arrivada')