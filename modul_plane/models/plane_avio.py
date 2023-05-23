from odoo import models, fields
class plane_avio(models.Model):
    _name = 'plane.avio'
    name = fields.Char(compute='_get_name', string="Nom complet", readonly='True', store=False)
    vols_ids = fields.One2many('plane.vol','avio_id', string = 'Vols') 
    imatge = fields.Char('Imatge')
    marca = fields.Integer('Marca')
    model = fields.Char('Model')
    maxvel = fields.Float('Maxima Velocitat')

    def _get_name(self):
        for record in self:
            record.name = str(record.marca) + " " + str(record.model)