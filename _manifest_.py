{
    'name': 'HM EOD Export Automation',
    'version': '1.0',
    'summary': 'Automates daily export of completed delivery orders',
    'category': 'Warehouse',
    'author': 'Your Name',
    'license': 'LGPL-3',
    'depends': ['stock', 'mail'],  # Dependencies needed
    'data': [
        'data/scheduled_action.xml',  # Scheduled job (to be created later)
    ],
    'installable': True,
    'application': False,
}