# -*- coding: utf-8 -*-
{
    'name': 'HM EOD Export Automation',
    'summary': 'Automates daily export of completed delivery orders',
    'category': 'Warehouse',
    'version': '1.0',
    'author': 'Your Name',
    'license': 'LGPL-3',
    'depends': ['stock', 'mail'],  # Dependencies needed
    'data': [
        'data/scheduled_action.xml',  # Scheduled job (to be created later)
    ],
}
