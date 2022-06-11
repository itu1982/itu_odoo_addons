from odoo import models,fields,api
from odoo.http import request
from datetime import datetime
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
from pprint import pprint
from odoo.addons.itu_log.models import itu_log
import logging, random

ItuLog = itu_log.ItuLog()

class ItuCompany(models.Model):
    _inherit = 'res.company'
  
    def write(self, values):
        res = super(ItuCompany, self).write(values)
        
        #Recogemos los datos de la ultima facturas
        UlFactura = self.env['account.move'].search([('company_id.id', '=', self.id)], limit=1, order="id desc") 
        
        if len(UlFactura) > 0:
            ItuLog.DebugText(' **************** Company -> Write: Factura Anterior encontrada -> ' + UlFactura.name)
            
            if UlFactura.compania.phone != self.phone or UlFactura.compania.email != self.email or UlFactura.compania.street != self.street or UlFactura.compania.street2 != self.street2 or UlFactura.compania.city != self.city or UlFactura.compania.state != self.state_id.name or UlFactura.compania.country != self.country_id.name or UlFactura.compania.vat != self.vat or UlFactura.compania.zip != self.zip or UlFactura.compania.partner_name != self.partner_id.name or UlFactura.compania.website != self.website or UlFactura.compania.name != self.name: 
            
                #Buscamos las facturas de esta compañia y les cambiamos el data_change_message  a True
                ItuLog.DebugText(' **************** Company -> Write: Company Modificado! -> Actualizando Facturas')
                facturas = self.env['account.move'].search([('company_id.id', '=', self.id)], order="id desc")   
                for record in facturas:
                    if record.data_change_message != True:
                        record.data_change_message = True
                        ItuLog.DebugText(' ****************COMP -> Fact. Modificada: ' + record.name )
            else:
                ItuLog.DebugText(' ****************COMP -> Write: Company NO modificado')
        else:
            ItuLog.DebugText(' ****************COMP -> Write: No tiene Facturas') 
            
        return res
