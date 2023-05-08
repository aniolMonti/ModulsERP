from odoo import models, fields
class zoo_especie(models.Model):
    _name = 'zoo.especie'
    id = fields.Integer('Id especie', required = True)
    familia = fields.Char('Familia')
    nomcientific = fields.Char('Nom cientific')
    nomvulgar = fields.Char('Nom vulgar')
    perill = fields.Char('Perill')