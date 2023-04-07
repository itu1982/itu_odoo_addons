#-*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.http import request
from datetime import datetime
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
from pprint import pprint
import logging, random
from odoo.addons.itu_log.models import itu_log

ItuLog = itu_log.ItuLog()

class ItuRepairInstallation (models.Model):
    _name = 'itu.venta_directa.installation'
    
    
    @api.model
    def ModuleDataInstallation(self):
        ItuLog.DebugText('*********Modificando parametros del modulo!*********') 
        param = self.env['ir.config_parameter'].sudo()
        ProductoVD = self.env['product.product'].search([('name', '=', 'VD')], limit=1, order="id desc") or False
        param.set_param('itu.venta_directa.ProductVD', ProductoVD.id)
        return {}