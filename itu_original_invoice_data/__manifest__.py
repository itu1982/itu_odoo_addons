# -*- coding: utf-8 -*-
{
    'name' : 'itu original invoice data',
    "summary": "Save Invoice Original Data in confirmation moment",
    "description": "Save Invoice Original Data in confirmation moment, when you reprint the invoice original data is recovered even if the customer's data has changed",
    "version": "14.0.0.0.1",
    "category": "Accounting",
    "website": "https://github.com/itu1982/itu_odoo_addons",
    "author": "Gorka Iturralde",
    "license": "AGPL-3",
    "support": "itusoftware@gmail.com",
    "depends": [
        'account',
        'itu_log',
    ],
    'data': [
        'security/ir.model.access.csv',
        'report/report_invoice_document.xml',
        'report/external_layout_background.xml',
        'views/account_move.xml',
        'report/external_layout_standard.xml',
        'report/external_layout_boxed.xml',
        'report/external_layout_clean.xml',        
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
