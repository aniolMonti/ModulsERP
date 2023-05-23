from odoo import models, fields
class plane_pilot(models.Model):
    _name = 'plane.pilot'
    name = fields.Char(compute='_get_name', string="Nom complet", readonly='True', store=False)
    vols_ids = fields.One2many('plane.vol','pilot_id', string = 'Vols') 
    nom = fields.Char('Nom')
    cognoms = fields.Char('Cognoms')
    nif = fields.Char('Nif')
    telf = fields.Char('Telefon')
    email = fields.Char('Email')

    def _get_name(self):
        for record in self:
            record.name = str(record.nom) + " " + str(record.cognoms)