# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO, Open Source Management Solution
#    Copyright (C) 2019 HLOUL-BAS (<http://www.hloul-bas.com>).
#
#    For Module Support : r2d2@hloul-bas.com 
#
##############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class AccountPayment(models.Model):
	_inherit = 'account.payment'

	activity_ids = fields.One2many('mail.activity', 'calendar_event_id', string='Activities')


class MailActivity(models.Model):
	_inherit = "mail.activity"

	calendar_event_id = fields.Many2one('calendar.event', string="Calendar Meeting", ondelete='cascade')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: