from odoo import models, fields
class zoo_animal(models.Model):
    _name = 'zoo.animal'
    name = fields.Char(compute='_get_name', string="Nom complet", readonly='True', store=False)
    zoo_id = fields.Many2one('zoo.zoo',string='Zoo')
    especie_id = fields.Many2one('zoo.especie',string='Especie')
    continentorigen = fields.Char('Continent d''origen')
    datanaix = fields.Date('Data de naixament')
    paisorigen = fields.Char("Pais d'origen")
    sexe = fields.Char('Sexe')

    def _get_name(self):
        for record in self:
            record.name = str(record.id) + " " + str(record.sexe)