# -*- coding: utf-8 -*-

import math
import re

from odoo import api, models


class AccountPayment(models.Model):
    _name = "account.payment"
    _inherit=['account.payment','mail.thread', 'mail.activity.mixin', 'utm.mixin', 'format.address.mixin']
