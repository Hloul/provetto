# -*- encoding: utf-8 -*-
#╔══════════════════════════════════════════════════════════════════╗
#║                                                                  ║
#║                ╔═══╦╗       ╔╗  ╔╗     ╔═══╦═══╗                 ║
#║                ║╔═╗║║       ║║ ╔╝╚╗    ║╔═╗║╔═╗║                 ║
#║                ║║ ║║║╔╗╔╦╦══╣╚═╬╗╔╬╗ ╔╗║║ ╚╣╚══╗                 ║
#║                ║╚═╝║║║╚╝╠╣╔╗║╔╗║║║║║ ║║║║ ╔╬══╗║                 ║
#║                ║╔═╗║╚╣║║║║╚╝║║║║║╚╣╚═╝║║╚═╝║╚═╝║                 ║
#║                ╚╝ ╚╩═╩╩╩╩╩═╗╠╝╚╝╚═╩═╗╔╝╚═══╩═══╝                 ║
#║                          ╔═╝║     ╔═╝║                           ║
#║                          ╚══╝     ╚══╝                           ║
#║ SOFTWARE DEVELOPED AND SUPPORTED BY ALMIGHTY CONSULTING SERVICES ║
#║                   COPYRIGHT (C) 2016 - TODAY                     ║
#║                   http://www.almightycs.com                      ║
#║                                                                  ║
#╚══════════════════════════════════════════════════════════════════╝
{
    'name': 'Discounts in Purchase order lines',
    'version': '1.0.1',
    'category': 'Purchase Management',
    'summary': 'Discounts in Purchase order lines',
    'description': """Discounts in Purchase order lines
    purchase discount discount on purchase purchase discounts
    line discount line discounts purchase line discount discount in purchase line
    purchase line discount""",
    'author': 'Almighty Consulting Services',
    'support': 'info@almightycs.com',
    'depends': ['stock', 'purchase','account'],
    'website': 'http://www.almightycs.com',
    'data': [
        "views/purchase_discount_view.xml",
        "views/report_purchaseorder.xml",
    ],
    'images': [
        'static/description/purchase_discount_almightycs_odoo_turkesh_patel.png',
    ],
    'application': False,
    'price': 14,
    'currency': 'EUR',
}
