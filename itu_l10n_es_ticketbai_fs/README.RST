=============================
itu_l10n_es_ticketbai_fs
=============================

Módulo que adapta los módulos de ticketbai (l10n_es_ticketbai_api y l10n_es_ticketbai) que puedes encontrar en https://github.com/OCA/l10n-spain/ para que puedas crear y rectificar facturas simplificadas desde la pantalla de Facturación/Contabilidad (Account.move) y que se envíen automaticamente a los servidores de TBAI.

* Si tenemos marcado al cliente como Anónimo (AEAT - Cliente anónimo) y el cliente no tiene DNI o CIF creara una factura simplificada.

* Crea un Diario de contabilidad (account.journal) para facturas simplificadas, de esta manera tendrán su propia secuencia y control. 

* Controla que el importe de la factura simplificada no sea superior al limite legal. Por defecto son 3000€. 

* Se puede usar con ticketbai Deshabilitado o habilitado.

* Adapta el archivo que se envia a ticketbai para indicar que es una factura simplificada o una rectificacion de una factura simplificada.

**Table of contents**

.. contents::
   :local:

Installation
============

Este módulo requiere de los módulos account, itu_log, l10n_es_ticketbai, itu_original_invoice_data y l10n_es_ticketbai_api.

Configuration
=============

* Por defecto el modulo se configura con un Diario nuevo para facturas simplificadas usando el código FS y con un limite para factura simplificada de 3000€

* Para configurar un cliente como anónimo: 
    * Ir a Contactos > Nombre_Contacto > Pestaña AEAT > 
    * Marcar al cliente como Anónimo (AEAT - Cliente anónimo)
    * Seleccionar como País (España) y Dejar el IVA/NIF/CIF en blanco.
    * Selecccionar como Posición fiscal "Régimen Nacional".

* El diario para facturas simplificadas puede configurarse en Configuración > Ajustes generales > empresas > Empresa > Pestaña Factura simplificada.

* El limite para las facturas simplificadas puede configurarse en Configuración > Ajustes generales > empresas > Empresa > Pestaña Factura simplificada.

Usage
=====

Al Crear una factura se comprueba si el cliente es anónimo y si tiene DNI/CIF. En ese caso se crea una factura simplificada en vez de una normal.

Known issues / Roadmap
======================

* El modulo da error al crear una factura simplificada si no tienes configurada la secuencia de facturas "normales" o si toca regenerarla, por ejemplo al cambiar de mes o año. Puedes solucionar este inconveniente simplemente generando una factura "normal". 


Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/itu1982/itu_odoo_addons/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/itu1982/itu_odoo_addons/issues/new?body=module:l10n_es_ticketbai_fs%0Aversion:14.0.0.0.2%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Gorka Iturralde.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
