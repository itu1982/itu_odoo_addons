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
    _inherit = 'account.move'
    #tbai_state = fields.Char(string='Use date', related='lot_id.use_date')
    tbai_state = fields.Selection(
        string="TBAI",
        selection=[
            (TicketBaiInvoiceState.draft.value, "Draft"),
            (TicketBaiInvoiceState.pending.value, "Pending"),
            (TicketBaiInvoiceState.sent.value, "Sent"),
            (TicketBaiInvoiceState.cancel.value, "Cancelled"),
            (TicketBaiInvoiceState.error.value, "Error"),
        ],
        default=TicketBaiInvoiceState.draft.value,
        index=True,
        copy=False,
        related='tbai_invoice_id.state'
    )

    tbai_general_state = fields.Selection(
        string="TBAI",
        selection=[
            (TicketBaiInvoiceState.draft.value, "Draft"),
            (TicketBaiInvoiceState.pending.value, "Pending"),
            (TicketBaiInvoiceState.sent.value, "Sent"),
            (TicketBaiInvoiceState.cancel.value, "Cancelled"),
            (TicketBaiInvoiceState.error.value, "Error"),
            ('Warning', "Warning"),
        ],
        default=TicketBaiInvoiceState.draft.value,
        index=True,
        copy=False,
        related='tbai_invoice_id.general_state'
    )
