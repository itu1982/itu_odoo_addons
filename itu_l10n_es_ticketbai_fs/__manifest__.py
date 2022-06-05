# -*- coding: utf-8 -*-
{
    'name' : 'Itu TicketBAI FS',
    "summary": "Agrega la posibilidad de crear facturas simplificadas desde facturacion/contabilidad.",
    "version": "14.0.0.0.6",
    "category": "Accounting & Finance",
    "website": "",
    "author": "Gorka Iturralde",
    "license": "AGPL-3",
    "support": "itusoftware@gmail.com",
    "depends": [
        'account',
        'point_of_sale',
        'l10n_es_ticketbai',
        'l10n_es_ticketbai_api',
        'itu_log',
        'itu_original_invoice_data',
    ],
    'data': [
#        'views/template.xml',
        'views/res_company.xml',
        'views/account_move.xml',
        'security/ir.model.access.csv',
        'data/data_tbai_fs.xml',
        'data/paper_format.xml',
        'report/ReceiptOrder2.xml',
        'report/ReceiptOrder.xml',
        'report/report_invoice_document.xml',
    ],
    'installable': True,
    'auto_install': True,
    'application': False,
}
