# -*- coding: utf-8 -*-
{
    'name' : 'Itu Venta Directa',
    "summary": "En ventas y facturacion asigna un producto a las lineas sin producto seleccionado",
    "version": "14.0.0.0.3",
    "category": "Extra Tools",
    "website": "https://github.com/itu1982/itu_odoo_addons",
    "author": "Gorka Iturralde",
    "license": "AGPL-3",
    "support": "itusoftware@gmail.com",
    "depends": [
        'account',
        'itu_log',
        'sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/datos_basicos.xml',
        'views/venta_directa_settings.xml',
    ],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
