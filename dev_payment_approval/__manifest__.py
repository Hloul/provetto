# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

{
    'name': 'Payment/Voucher Double Approval Workflow',
    'version': '12.0.1.0',
    'sequence': 1,
    'category': 'Accounting',
    'description':
        """
        This Module add below functionality into odoo

        1.Manager have to validate payments before Confirmation -- two or three step process
        2.This module helps you to set limit on Payments, So, Manager must have validate Payment if it exceed the Per-Defined Limit before Confirmation.
        3.Flow will be two step or three step based on conditions
        
        odoo payment approval 
        Odoo double payment approval
        odoo payment voucher approval 
 
Payment approval 
Odoo payment approval 
Helps you to Verify Payment before Confirming it
Odoo Helps you to Verify Payment before Confirming it
Payment Approvals 
Odoo payment approvals 
Manage payment 
Odoo manage payment 
Manage payment approval 
Odoo manage payment approval 
Create payment approval 
Odoo create payment approval 
Set payment approval process 
Odoo set payment approval process 
Set payment process 
Odoo set payment process 
Payment process 
Odoo payment process 
Set payment process approval 
Odoo set payment process approval
       
        

    """,
    'summary': 'odoo app manage payment two three way approval process workflow',
    'depends': ['account'],
    'data': [
        'security/security.xml',
        'views/view_res_config_settings.xml',
        'views/account_payment_view.xml',
    ],
    'demo': [],
    'test': [],
    'css': [],
    'qweb': [],
    'js': [],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    
    #author and support Details
    'author': 'DevIntelle Consulting Service Pvt.Ltd',
    'website': 'http://www.devintellecs.com',    
    'maintainer': 'DevIntelle Consulting Service Pvt.Ltd', 
    'support': 'devintelle@gmail.com',
    'price':25.0,
    'currency':'EUR',
    #'live_test_url':'https://youtu.be/A5kEBboAh_k',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
