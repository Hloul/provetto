# -*- coding: utf-8 -*-

from odoo import api, fields, models
import odoo.addons.decimal_precision as dp


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    @api.depends('discount')
    def _compute_amount(self):
        prices = {}
        for line in self:
            if line.discount:
                prices[line.id] = line.price_unit
                line.price_unit *= (1 - line.discount / 100.0)
            super(PurchaseOrderLine, line)._compute_amount()
            if line.discount:
                line.price_unit = prices[line.id]

    discount = fields.Float(
        string='Discount (%)', digits=dp.get_precision('Discount'))

    _sql_constraints = [
        ('discount_limit', 'CHECK (discount <= 100.0)',
         'Discount must be lower than 100%.'),
    ]

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    def _prepare_invoice_line_from_po_line(self, line):
        res = super(AccountInvoice, self)._prepare_invoice_line_from_po_line(line)
        res['discount'] = line.discount
        return res


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    @api.onchange('purchase_line_id','product_id')
    def onchange_purchase_line_id(self):
        if self.purchase_line_id:
            self.discount = self.purchase_line_id.discount
