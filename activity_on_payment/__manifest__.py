# -*- coding: utf-8 -*-

{
    'name': 'Activity on Payment',
    'version': '1.0',
    'category': 'Accounting',
    'sequence': 6,
    'author': 'HLOUL-BAS',
    'summary': 'Add activity scheduling to payments',
    'description': """
HLOUL-BAS
=======================
Add the functionality of schedule an activity to payments model

""",
    'depends': ['mail','account'],
    'data': [
        'views/views.xml',
    ],
    'installable': True,
    'website': 'www.hloul-bas.com',
    'auto_install': False,
}
