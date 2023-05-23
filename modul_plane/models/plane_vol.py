from odoo import models, fields
class plane_vol(models.Model):
    _name = 'plane.vol'
    name = fields.Char(compute='_get_name', string="Nom complet", readonly='True', store=False)
    avio_id = fields.Many2one('plane.avio',string='Avio')
    pilot_id = fields.Many2one('plane.pilot',string='Pilot')
    desti = fields.Many2one('plane.aeroport',string='Desti')
    origen = fields.Many2one('plane.aeroport',string='Origen')
    passatgers = fields.Integer('Passatgers')
    datasortida = fields.Datetime('Data Sortida')
    dataarrivada = fields.Datetime('Data Arrivada')

    def _get_name(self):
        for record in self:
            record.name = str(record.id)