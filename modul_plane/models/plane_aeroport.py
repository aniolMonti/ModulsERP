from odoo import models, fields
class plane_aeroport(models.Model):
    _name = 'plane.aeroport'
    nom = fields.Char('Nom')
    imatge = fields.Char('Imatge')
    ciutat = fields.Char('Ciutat')
    pais = fields.Char('Pais')
    latitud = fields.Float('Latitut')
    longitut = fields.Float('Longitut')