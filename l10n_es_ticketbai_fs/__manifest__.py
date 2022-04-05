# -*- coding: utf-8 -*-
{
    'name' : 'TicketBAI FS',
    "summary": "Agrega la posibilidad de crear facturas simplificadas desde facturacion/contabilidad.",
    "version": "14.0.0.0.4",
    "category": "Accounting & Finance",
    "website": "",
    "author": "Gorka Iturralde",
    "license": "AGPL-3",
    "depends": [
        'account',
        'l10n_es_ticketbai',
        'l10n_es_ticketbai_api',
        'itu_log',
    ],
    'data': [
        'views/res_company.xml',
        'security/ir.model.access.csv',
        'data/data_tbai_fs.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
