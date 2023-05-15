from odoo import models, fields
class plane_avio(models.Model):
    _name = 'plane.avio'
    imatge = fields.Char('Imatge')
    marca = fields.Integer('Marca')
    model = fields.Char('Model')
    maxvel = fields.Float('Maxima Velocitat')