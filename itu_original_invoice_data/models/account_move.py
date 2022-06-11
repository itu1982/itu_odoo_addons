from odoo import models,fields,api
from odoo.http import request
from datetime import datetime
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
from pprint import pprint
from odoo.addons.itu_log.models import itu_log
import logging, random

ItuLog = itu_log.ItuLog()

class ItuAccountMoveInPartner (models.Model):
    _inherit = 'account.move'
    cliente = fields.Many2one ('itu.invoice.partner', string='Customer:', required=True)
    compania = fields.Many2one ('itu.invoice.company', string='Company:', required=True)
    
    data_change_message = fields.Boolean ('Parted changed',
        default=False,
        store=True,
        index=True,
        copy=False,
    ) 

    def action_post(self):
        
        #Nos copiamos el Partner (Cliente) para guardarlo junto con la factura.
        ItuLog.DebugText(" ************** ITU INVOICE PARTNER - ACTION POST ************** ")
        ClienteNew = self.env['itu.invoice.partner'].create ([{'name': self.partner_id.name, 'street': self.partner_id.street, 'street2': self.partner_id.street2, 'zip': self.partner_id.zip, 'city': self.partner_id.city, 'state': self.partner_id.state_id.name, 'country': self.partner_id.country_id.name, 'vat': self.partner_id.vat, 'email': self.partner_id.email}])
        
        self.cliente = ClienteNew
        
        #Ahora nos guardamos los datos de la compañia junto con la factura.
        ItuLog.DebugText(" ************** ITU INVOICE COMPANY - ACTION POST ************** ")
        CompanyNew = self.env['itu.invoice.company'].create ([{'name': self.company_id.name, 'street': self.company_id.street, 'street2': self.company_id.street2, 'zip': self.company_id.zip, 'city': self.company_id.city, 'state': self.company_id.state_id.name, 'country': self.company_id.country_id.name, 'vat': self.company_id.vat, 'email': self.company_id.email, 'phone': self.company_id.phone, 'partner_name': self.company_id.partner_id.name,  'website': self.company_id.website}])
        
        self.compania = CompanyNew
                 
        result = super(ItuAccountMoveInPartner, self).action_post()
        return result