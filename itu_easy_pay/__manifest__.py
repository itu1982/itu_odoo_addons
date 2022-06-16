# -*- coding: utf-8 -*-
{
    'name' : 'Itu Easy Pay',
    "summary": "Register you payments easy",
    "version": "14.0.0.0.1",
    "category": "Accounting & Finance",
    "website": "https://github.com/itu1982/itu_odoo_addons",
    "author": "Gorka Iturralde",
    "license": "AGPL-3",
    "support": "itusoftware@gmail.com",
    "depends": [
        'account',
        'itu_log',
        'payment',
    ],
    'data': [
        'views/account_payment_register_views.xml',
        'views/account_move.xml',
        'security/ir.model.access.csv',
    ],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
