# -*- coding: utf-8 -*-

import math
import re

from odoo import api, models


class StockInventory(models.Model):
    _name = "stock.inventory"
    _inherit=['stock.inventory','mail.thread', 'mail.activity.mixin', 'utm.mixin', 'format.address.mixin']
