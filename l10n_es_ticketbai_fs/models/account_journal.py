from odoo import models,fields,api
from odoo.http import request
from datetime import datetime
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
from pprint import pprint
from odoo.addons.itu_log.models import itu_log
import logging, random

ItuLog = itu_log.ItuLog()

class ItuJournalSeqByYear(models.Model):
    _inherit = 'account.journal'
    
    @api.model
    def _add_first_fs_data(self):    
        ItuLog.DebugText(" **************** _ADD TBAI FS FIRST DATA ************** ")
        #Buscamos las empresas existentes
        #Añadimos en todas las empresas un Diario de facturas simplificadas.
        Empresas = self.env['res.company'].search([])   
        if len(Empresas) > 0:
            for Empresa in Empresas:
                ItuLog.DebugText(" **************** FOR EMPRESAS ************** ")
                #Controlamos que el diario no este creado ya, añadimos el diario y configuramos tbai_fs.
                if self.env['account.journal'].search_count([('name','=', 'Facturas Simplificadas de Clientes (' + Empresa.name + ')')]) == 0:
                    ItuLog.DebugText(" **************** AGREGAMOS ************** ")
                    record = {
                    'name': 'Facturas Simplificadas de Clientes (' + Empresa.name + ')',
                    'code': 'FS', 
                    'company_id': Empresa.id,
                    'invoice_reference_model': 'odoo', 
                    'invoice_reference_type': 'invoice',   
                    'type': 'sale',
                    }
                    JournalNew = self.create (record)
                    Empresa.tbai_fs_journal_id = JournalNew
                    Empresa.tbai_fs_limit = 3000
                   