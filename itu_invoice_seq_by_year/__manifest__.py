# -*- coding: utf-8 -*-
{
    'name' : 'Sequence by Year - Secuencias por Año',
    "summary": "Permite configurar las secuencias como FACT / AÑO / Numero, sin que aparecezca el mes..",
    "version": "14.0.0.0.3",
    "category": "Accounting & Finance",
    "website": "",
    "author": "Gorka Iturralde",
    "license": "AGPL-3",
    "support": "itusoftware@gmail.com",
    "depends": [
        'account',
        'itu_log',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/account_journal.xml',
    ],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
