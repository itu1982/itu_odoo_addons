=============================
ITU LOG
=============================

Módulo que permite enviar mensajes al archivo log, siempre y cuando estemos 
en modo Debug.

**Table of contents**

.. contents::
   :local:

Installation
============

Este módulo no requiere ningún modulo especial. 

Configuration
=============

Instalar modulo desde aplicaciones. 

Usage
=====

Importando el modulo de la siguiente manera: 

from odoo.addons.itu_log.models import itu_log
ItuLog = itu_log.ItuLog()

Nos permite enviar mensajes al archivo log configurado en odoo  usando el comando:

ItuLog.DebugText(" **************** ACTION POST ************** ")

Antes de enviarse el mensaje comprueba que odoo este en modo debug. 


Known issues / Roadmap
======================


Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/itu1982/itu_odoo_addons/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/itu1982/itu_odoo_addons/issues/new?body=module:itu_log%0Aversion:14.0.0.0.2%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Gorka Iturralde.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
