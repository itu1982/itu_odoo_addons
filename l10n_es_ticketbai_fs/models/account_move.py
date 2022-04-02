from odoo import models,fields,api
from odoo.http import request
from datetime import datetime
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
from pprint import pprint
from odoo.addons.itu_log.models import itu_log
import logging, random

from odoo.addons.l10n_es_ticketbai_api.models.ticketbai_invoice import (
    RefundCode,
    RefundType,
    SiNoType,
    TicketBaiInvoiceState,
)

ItuLog = itu_log.ItuLog()

class TbaiAccountMoveFS(models.Model):
    _inherit = 'account.move'

    def action_post(self):
        ItuLog.DebugText(" **************** ACTION POST ************** ")
        if not self.partner_id.vat and self.partner_id.aeat_anonymous_cash_customer:
            ItuLog.DebugText(" **************** CAMBIO DIARIO ************** ")
            self.journal_id = self.company_id.tbai_fs_journal_id
        else:
            ItuLog.DebugText(" **************** DNI ENCONTRADO ************** " + str(self.partner_id.vat))    
            
        result = super(TbaiAccountMoveFS, self).action_post()
        return result
        
    @api.onchange("reversed_entry_id")
    def onchange_tbai_reversed_entry_id(self):
        if self.reversed_entry_id:
            if not self.partner_id.vat and self.partner_id.aeat_anonymous_cash_customer:
                self.tbai_refund_key = RefundCode.R5.value
        result = super(TbaiAccountMoveFS, self).onchange_tbai_reversed_entry_id()

#    @api.model_create_multi
#    def create(self, vals):
        
#        result = super(TbaiFS, self).create(vals)
#        ItuLog.DebugText(" **************** FAC SIMP CREANDO ************** ")

#        return result
        
        
#    @api.model_create_multi
#    def write(self, vals):
        
#        ItuLog.DebugText(" **************** FAC ESCRIBIENDO ************** ")
        
#        result = super(TbaiFS, self).write(vals)
#        return result
        
    def Fact_Simplificada(self):
        ItuLog.DebugText(" **************** FACT. SIMP. MESCRIBIENDO ************** ")
        #self.tbai_invoice_id.simplified_invoice = SiNoType.S.value
        #self.partner_id = 11
        #self.journal_id = 20
        self.action_post()
        return False

