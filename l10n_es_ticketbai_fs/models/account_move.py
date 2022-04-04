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
    tbai_refund_key = fields.Selection(selection_add=[(RefundCode.R5.value, 'Factura rectificativa simplificada'),],)
    
#    tbai_refund_key = fields.Selection(
#        selection=[
#            (RefundCode.R1.value, "Art. 80.1, 80.2, 80.6 and rights founded error"),
#            (RefundCode.R2.value, "Art. 80.3"),
#            (RefundCode.R3.value, "Art. 80.4"),
#            (RefundCode.R4.value, "Art. 80 - other"),
#            (RefundCode.R5.value, "Rectificacion de Factura simplificada"),
#        ],
#        help="BOE-A-1992-28740. Ley 37/1992, de 28 de diciembre, del Impuesto sobre el "
#        "Valor Añadido. Artículo 80. Modificación de la base imponible.",
#        copy=False,
#    )

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

