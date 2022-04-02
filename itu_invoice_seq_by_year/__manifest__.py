# -*- coding: utf-8 -*-
{
    'name' : 'Sequence by Year - Secuencias por Año',
    "summary": "Permite configurar las secuencias como FACT / AÑO / Numero, sin que aparecezca el mes..",
    "version": "14.0.0.0.2",
    "category": "Accounting & Finance",
    "website": "",
    "author": "Gorka Iturralde",
    "license": "AGPL-3",
    "depends": [
        'account',
        'itu_log',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/account_journal.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}