# -*- coding: utf-8 -*-
{
    'name' : 'Itu Tbai Status',
    "summary": "Muestra el estado del envio en la lista de facturas",
    "version": "14.0.0.0.2",
    "category": "Extra Tools",
    "website": "https://github.com/itu1982/itu_odoo_addons",
    "author": "Gorka Iturralde",
    "license": "AGPL-3",
    "support": "itusoftware@gmail.com",
    "depends": [
        'account',
        'itu_log',
        'l10n_es_ticketbai',
        'l10n_es_ticketbai_api',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/account_move.xml',
    ],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
