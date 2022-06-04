from odoo import models,fields,api
from odoo.http import request
from datetime import datetime
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
from pprint import pprint
from odoo.addons.itu_log.models import itu_log
import logging, random

ItuLog = itu_log.ItuLog()

class ItuPartner (models.Model):
    _inherit = 'res.partner'
  
    def write(self, values):
        res = super(ItuPartner, self).write(values)
        
        #Recogemos los datos de la ultima facturas
        UlFactura = self.env['account.move'].search([('partner_id.id', '=', self.id)], limit=1, order="id desc") 
        
        if len(UlFactura) > 0:
            ItuLog.DebugText(' **************** Cliente -> Write: Factura Anterior encontrada -> ' + UlFactura.name)
            
            if UlFactura.cliente.email != self.email or UlFactura.cliente.street != self.street or UlFactura.cliente.street2 != self.street2 or UlFactura.cliente.city != self.city or UlFactura.cliente.state != self.state_id.name or UlFactura.cliente.country != self.country_id.name or UlFactura.cliente.vat != self.vat or UlFactura.cliente.zip != self.zip or UlFactura.cliente.name != self.name: 

                #Buscamos las facturas de esta compañia y les cambiamos el data_change_message  a True
                ItuLog.DebugText(' **************** Cliente -> Write: Cliente Modificado! -> Actualizando Facturas')
                facturas = self.env['account.move'].search([('partner_id.id', '=', self.id)], order="id desc")   
                for record in facturas:
                    record.data_change_message = True
                    ItuLog.DebugText(' **************** Cliente -> Write: Factura Modificada -> ' + record.name )
            else:
                ItuLog.DebugText(' ****************Cliente -> Write: Cliente NO modificado')
        else:
            ItuLog.DebugText(' **************** Cliente -> Write: Cliente No tiene Facturas') 
    
        return res