from odoo import api, fields, models, _


class RelatedModule(models.Model):
    _name = "project.odoo.module"
    _description = 'Related Module'

    name = fields.Char(string="Name")

