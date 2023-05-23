from odoo import models, fields
class plane_aeroport(models.Model):
    _name = 'plane.aeroport'
    name = fields.Char(compute='_get_name', string="Nom complet", readonly='True', store=False)
    nom = fields.Char('Nom')
    desti = fields.One2many('plane.vol','desti', string = 'Vols de destí') 
    origen = fields.One2many('plane.vol','origen', string = "Vols d'origen") 
    imatge = fields.Char('Imatge')
    ciutat = fields.Char('Ciutat')
    pais = fields.Char('Pais')
    latitud = fields.Float('Latitud')
    longitut = fields.Float('Longitud')

    def _get_name(self):
        for record in self:
            record.name = str(record.nom) + " " + str(record.ciutat)