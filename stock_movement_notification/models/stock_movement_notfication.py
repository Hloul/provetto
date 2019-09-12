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


class stockmovementnotfication(models.Model):
	_inherit = ['stock.inventory', 'mail.thread', 'mail.activity.mixin']
	_name = "stock.inventory"
