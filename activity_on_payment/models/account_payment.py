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
     #_inherit = ['account.payment','mail.activity.mixin']
	activity_ids = fields.One2many('mail.activity', string='Activities')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: