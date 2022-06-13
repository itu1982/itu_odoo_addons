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
        
        #Para que no de error de singleton en res_company
        for registro in self:
        
            #Recogemos los datos de la ultima facturas
            UlFactura = self.env['account.move'].search([('company_id.id', '=', registro.id)], limit=1, order="id desc") 
            
            if len(UlFactura) > 0:
                ItuLog.DebugText(' **************** Company -> Write: Factura Anterior encontrada -> ' + UlFactura.name)
                
                if UlFactura.compania.phone != registro.phone or UlFactura.compania.email != registro.email or UlFactura.compania.street != registro.street or UlFactura.compania.street2 != registro.street2 or UlFactura.compania.city != registro.city or UlFactura.compania.state != registro.state_id.name or UlFactura.compania.country != registro.country_id.name or UlFactura.compania.vat != registro.vat or UlFactura.compania.zip != registro.zip or UlFactura.compania.partner_name != registro.partner_id.name or UlFactura.compania.website != registro.website or UlFactura.compania.name != registro.name: 
                
                    #Buscamos las facturas de esta compañia y les cambiamos el data_change_message  a True
                    ItuLog.DebugText(' **************** Company -> Write: Company Modificado! -> Actualizando Facturas')
                    facturas = self.env['account.move'].search(['&',('company_id.id', '=', registro.id), ('state', '!=', 'draft')], order="id desc")   
                    for record in facturas:
                        if record.data_change_message != True:
                            record.data_change_message = True
                            ItuLog.DebugText(' ****************COMP -> Fact. Modificada: ' + record.name )
                else:
                    ItuLog.DebugText(' ****************COMP -> Write: Company NO modificado')
            else:
                ItuLog.DebugText(' ****************COMP -> Write: No tiene Facturas') 
            
        return res
