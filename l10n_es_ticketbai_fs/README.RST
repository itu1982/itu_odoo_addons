=============================
l10n_es_ticketbai_fs
=============================

Módulo que adapta los modulos de ticketbai (l10n_es_ticketbai_api y l10n_es_ticketbai) que 
puedes encontrar en https://github.com/OCA/l10n-spain/ para que puedas crear y rectificar 
facturas simplificadas desde la pantalla de Facturacion/Contabilidad (Account.move) y que se envien
automaticamente a los servidores de TBAI.

* Crea un Diario de contabilidad (account.journal) para facturas simplificadas, de esta manera tendran su propia secuencia y control. El diario para facturas simplificadas puede configurarse en Configuracion > Ajustes generales > empresas > Empresa > Pestaña TicketBAI.

* Controla que el importe de la factura simplificada no sea superior al limite legal. Por defecto son 3000€. El limite es configurable en Configuracion > Ajustes generales > empresas > Empresa > Pestaña TicketBAI.

**Table of contents**

.. contents::
   :local:

Installation
============

Este módulo requiere de los módulos `account` y `itu_log`.

Configuration
=============

Una vez instalado, ir a la configuración del Diario (Journal) y activar
el checkbox "Secuencias por año" de la configuración. Los nuevos diarios que se creen
tendrán esta opción activada por defecto. 

Usage
=====

Al Crear o Regenerar una secuencia en vez de comenzar con CODIGO / AÑO / MES / Nº FACTURA
se crea uno CODIGO / AÑO / Nº FACTURA. 

Nota: Al crear una entrada en un díario la secuencia se coge de la ultima entrada, por lo tanto
si el Diario ya tenia entradas usando la secuencita CODIGO / AÑO / MES / Nº FACTURA no cambiara 
hasta que toque regenerarla, por ejemplo con el cambio de mes. 

Known issues / Roadmap
======================


Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/itu1982/itu_odoo_addons/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/itu1982/itu_odoo_addons/issues/new?body=module:itu_invoice_seq_by_year%0Aversion:14.0.0.0.2%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Gorka Iturralde.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
