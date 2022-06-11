=============================
ITU TBAI STATUS
=============================

Muestra una columna con el estado de TBAI en el listado de facturas.


**Table of contents**

.. contents::
   :local:

Installation
============

Este módulo requiere de los módulos `account` , `itu_log`, `l10n_es_ticketbai` y `l10n_es_ticketbai_api`

Configuration
=============

Una vez instalado, aparecera una columna nueva en la lista de facturas. 

Usage
=====

Funciona automaticamente con las facturas nuevas.  

Contiene los siguientes estados:

- Borrador: La factura aun no ha sido confirmada y por tanto no se ha enviado. 

- Pendiente: La factura esta en cola para ser enviada.

- Enviada: Enviada y recibida correctamente

- Atencion: Ha habido algun contratiempo al enviar la factura, es necesario revisar los mensajes recibidos desde TBAI.

- Error: Se ha producido un error grave al enviar la factura o a sido cancelada.

Nota: Marcando la factura "Para revisar" dentro de la factura > "otra informacion" se recalcula el estado.

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
