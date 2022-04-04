=============================
ITU INVOICE SEQUENCE BY YEAR
=============================

Módulo que adapta la secuencia a Codigo/Año/Numero Factura:

* Crea un checkbox en los Diarios de contabilidad (account.journal) para activar
  o desactivar la secucia usando solo el año. 

**Table of contents**

.. contents::
   :local:

Installation
============

Este módulo requiere de los módulos `account` y `itu_log`.

Configuration
=============

Una vez instalado, ir a la configuración del Diario (Journal) y activar
el checkbox "Secuencias por año" de la configuración. Los nuevos Diarios que se creen
tendrán esta opción activada por defecto. 

Usage
=====

Cuenta toca Crear o Regenerar una secuencia en vez de comenzar con CODIGO / AÑO / MES / Nº FACTURA
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
`feedback <https://github.com/OCA/l10n-spain/issues/new?body=module:%20l10n_es_aeat%0Aversion:%2015.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Gorka Iturralde.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
