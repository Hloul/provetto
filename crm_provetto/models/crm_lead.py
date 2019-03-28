# -*- coding: utf-8 -*-

import logging
from datetime import timedelta
from functools import partial

import psycopg2


from odoo import api, fields, models, tools, _
from odoo.tools import float_is_zero
from odoo.exceptions import UserError
from odoo.http import request
import odoo.addons.decimal_precision as dp

_logger = logging.getLogger(__name__)

class pos_config(models.Model):
    _inherit = 'crm.lead'
    #is_blacklisted=fields.Boolean(string='Is Blacklisted') 
        
        
    



