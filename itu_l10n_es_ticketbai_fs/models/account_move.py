from odoo import models,fields,api
from odoo.http import request
from datetime import datetime
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
from pprint import pprint
from odoo import _
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
    tbai_refund_key = fields.Selection(selection_add=[(RefundCode.R5.value, 'Simplified Refund invoice'),],)
    invoice_datetime = fields.Datetime('Invoice Date')
       
    def action_post(self):
        ItuLog.DebugText(" **************** ACTION POST ************** ")
        
        #Cuidado con el error singleton
        for registro in self:
            registro.invoice_datetime = datetime.now()
            if not registro.partner_id.vat and registro.partner_id.aeat_anonymous_cash_customer:
                ItuLog.DebugText(" **************** CAMBIO DIARIO ************** ")
                registro.journal_id = registro.company_id.tbai_fs_journal_id
            else:
                ItuLog.DebugText(" **************** DNI ENCONTRADO ************** " + str(registro.partner_id.vat))    
                
        result = super(TbaiAccountMoveFS, self).action_post()
        return result
        
    @api.onchange("reversed_entry_id")
    def onchange_tbai_reversed_entry_id(self):
        ItuLog.DebugText(" **************** onchange_tbai_reversed_entry_id ************** ")
        if self.reversed_entry_id:
            if not self.partner_id.vat and self.partner_id.aeat_anonymous_cash_customer:
                ItuLog.DebugText(" **************** onchange_tbai_reversed_entry_id R5 ************** ")
                self.tbai_refund_key = RefundCode.R5.value
        result = super(TbaiAccountMoveFS, self).onchange_tbai_reversed_entry_id()
        
    def tbai_is_invoice_refund(self):
        ItuLog.DebugText(" **************** tbai_is_invoice_refund ************** ")
        result = super(TbaiAccountMoveFS, self).tbai_is_invoice_refund()
        if result and not self.partner_id.vat and self.partner_id.aeat_anonymous_cash_customer:
            ItuLog.DebugText(" **************** tbai_is_invoice_refund R5 ************** ")
            self.tbai_refund_key = RefundCode.R5.value    
        return result
        
    @api.model_create_multi
    def create(self, vals_list):
        ItuLog.DebugText(" **************** Tbai FS AC.MV CREATE ************** ")
        for vals in vals_list:
            if 'invoice_datetime' in vals:
                ItuLog.DebugText(" **************** Guardando fecha ************** ")
                vals["invoice_datetime"] = datetime.now()
                
        rslt = super(TbaiAccountMoveFS, self).create(vals_list)
        return rslt
        


