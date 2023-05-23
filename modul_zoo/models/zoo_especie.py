from odoo import models, fields
class zoo_especie(models.Model):
    _name = 'zoo.especie'
    name = fields.Char(compute='_get_name', string="Nom complet", readonly='True', store=False)
    animals_ids = fields.One2many('zoo.animal','especie_id', string = 'Animals') 
    familia = fields.Char('Familia')
    nomcientific = fields.Char('Nom cientific')
    nomvulgar = fields.Char('Nom vulgar')
    perill = fields.Char('Perill')

    def _get_name(self):
        for record in self:
            record.name = str(record.nomvulgar) + " " + str(record.familia)