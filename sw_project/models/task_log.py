from odoo import api, fields, models, _
from datetime import datetime


class TaskLog(models.Model):
    _name = 'project.task.log'

    description = fields.Char(string="Description")
    related_task_id = fields.Many2one('project.task', string="Related Task", required=True)
    project_id = fields.Many2one('project.project', string="Project")
    logged_by = fields.Many2one('res.partner',
                                string='Logged By',
                                required=True)
    logged_on = fields.Date(String="Logged On", default=fields.Date.today())
    log_source = fields.Char(string="Log Source")
    related_meeting = fields.Char(string="Related Meeting")
    log_type = fields.Selection(selection=[('bug_log', 'Bug Log'),
                                           ('change_request_log', 'Change Request Log'),
                                           ('risk_log', 'Risk Log'),
                                           ('decision_log', 'Decision Log'),
                                           ('information_log', 'Information Log')],
                                string="Log Type")

    # @api.model
    # def create(self, vals):
    #     res = super(TaskLog, self).create(vals)
    #     if res.log_type == 'bug_log':
    #         seq_no = self.env['ir.sequence'].next_by_code('project.task.log.bug')
    #         res.write({
    #             'name': seq_no,
    #         })
    #     elif res.log_type == 'change_request_log':
    #         seq_no = self.env['ir.sequence'].next_by_code('project.task.log.change.request.log')
    #         res.write({
    #             'name': seq_no,
    #         })
    #     elif res.log_type == 'risk_log':
    #         seq_no = self.env['ir.sequence'].next_by_code('project.task.log.risk.log')
    #         res.write({
    #             'name': seq_no,
    #         })
    #     elif res.log_type == 'decision_log':
    #         seq_no = self.env['ir.sequence'].next_by_code('project.task.log.decision.log')
    #         res.write({
    #             'name': seq_no,
    #         })
    #     elif res.log_type == 'information_log':
    #         seq_no = self.env['ir.sequence'].next_by_code('project.task.log.information.log')
    #         res.write({
    #             'name': seq_no,
    #         })
    #     return res

    def action_log_form_view(self):
        action = self.env["ir.actions.actions"]._for_xml_id("sw_project.view_project_task_log_action")
        action['res_id'] = self.id
        action['view_id'] = self.env.ref('sw_project.project_task_log_view_form').id
        action['view_type'] = 'form'
        action['view_mode'] = 'form'
        del action['views']

        return action

    def action_new_task_view(self):
        if self.log_type =="change_request_log":
            action = self.env["ir.actions.actions"]._for_xml_id("project.action_view_task")
            action['context'] = {'default_display_project_id': self.project_id.id,'default_parent_id':self.related_task_id.id,'default_description':self.description}
            action['view_id'] = self.env.ref('sw_project.view_task_inherit_view_task_form2').id
            action['view_type'] = 'form'
            action['view_mode'] = 'form'
            del action['views']
        else:
            action = self.env["ir.actions.actions"]._for_xml_id("project.action_view_task")
            action['context'] = {'default_project_id': self.project_id.id, 'default_description':self.description}
            action['view_id'] = self.env.ref('sw_project.view_task_inherit_view_task_form2').id
            action['view_type'] = 'form'
            action['view_mode'] = 'form'
            del action['views']

        return action
