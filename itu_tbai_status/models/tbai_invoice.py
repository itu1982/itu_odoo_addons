from odoo import models,fields,api
from odoo.http import request
from datetime import datetime
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
from pprint import pprint
from odoo.addons.itu_log.models import itu_log
import logging, random

ItuLog = itu_log.ItuLog()

from odoo.addons.l10n_es_ticketbai_api.models.ticketbai_invoice import (
    RefundCode,
    RefundType,
    SiNoType,
    TicketBaiInvoiceState,
)

class TbaiStateAccountMove(models.Model):
    _inherit = 'tbai.invoice'
    general_state = fields.Selection(
        string="TBAI",
        selection=[
            (TicketBaiInvoiceState.draft.value, "Draft"),
            (TicketBaiInvoiceState.pending.value, "Pending"),
            (TicketBaiInvoiceState.sent.value, "Sent"),
            (TicketBaiInvoiceState.cancel.value, "Cancelled"),
            (TicketBaiInvoiceState.error.value, "Error"),
            ('Warning', "Warning"),
        ],
        compute='_compute_tbai_general_state',
        store=True,
        default=TicketBaiInvoiceState.draft.value,
        index=True,
        copy=False,
    )
    
    @api.depends(
        "tbai_response_ids.tbai_response_message_ids.code",
        "state",
        "invoice_id.to_check",
    )
    def _compute_tbai_general_state(self):
        ItuLog.DebugText(' **************** Compute G State  ****************') 
        #Cogemos el valor de state y lo modificamos solo en caso de que sea necesario.
        #Por ejemplo si hay mas de un mensaje de respuesta lo cambiamos a Warning
        self.general_state = self.state
        if self.general_state == TicketBaiInvoiceState.sent.value and len(self.tbai_response_ids.tbai_response_message_ids) > 1:
            self.general_state = "Warning"
            
            #respuestas = self.tbai_response_ids
            #respuestas.sorted(key='write_date')    
            #for respuesta in respuestas:
            #    general_state == TicketBaiInvoiceState.sent.value
            #    if 
         