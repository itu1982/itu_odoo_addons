from odoo import _, api, exceptions, fields, models
from datetime import datetime
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
from pprint import pprint
from odoo.addons.itu_log.models import itu_log
import logging, random
from odoo.addons.l10n_es_ticketbai_api.utils import utils as tbai_utils

class SiNoType(tbai_utils.EnumValues):
    S = "S"
    N = "N"

ItuLog = itu_log.ItuLog()

from odoo.addons.l10n_es_ticketbai_api.models.ticketbai_invoice import (
    RefundCode,
    RefundType,
    SiNoType,
    TicketBaiInvoiceState,
)

class TbaiInvoiceFS(models.Model):
    _inherit = 'tbai.invoice'
    refund_code = fields.Selection(selection_add=[(RefundCode.R5.value, 'Simplified refund invoice'),],)

    @api.constrains("simplified_invoice")
    def _check_simplified_invoiceFS(self):
        ItuLog.DebugText(" **************** _check_simplified_invoiceFS ************** ")
        for record in self:
            if record.simplified_invoice == SiNoType.S.value and record.invoice_id.amount_total > self.company_id.tbai_fs_limit:
                raise exceptions.ValidationError( _("a Simple Invoice %s can`t be more than %d") % (record.name, self.company_id.tbai_fs_limit))
            #else:
                #record.invoice_id.journal_id = self.company_id.tbai_fs_journal_id
                
