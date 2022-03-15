from odoo import api, fields, models, _


class TaskType(models.Model):
    _name = "project.task.subtype"
    _description = 'Task type'

    name = fields.Char(string="Name")
