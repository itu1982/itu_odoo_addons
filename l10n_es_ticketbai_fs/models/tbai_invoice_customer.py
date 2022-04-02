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

class TbaiInvoiceCustomerFS(models.Model):
    _inherit = 'tbai.invoice.customer'
       
    @api.constrains("identification_number")
    def _check_identification_number(self):
        ItuLog.DebugText(" **************** CHECK IDENT NUMBER FS ************** ")
        for record in self:
            if not record.nif and record.tbai_invoice_id.invoice_id.partner_id.aeat_anonymous_cash_customer:
                ItuLog.DebugText(" **************** ANONIMOOOO FS ************** ")
                record.tbai_invoice_id.simplified_invoice = SiNoType.S.value
            else:
                ItuLog.DebugText(" **************** NO ANONIMO - QUE LO COMPRUEBEN ************** ")
                result = super(TbaiInvoiceCustomerFS, self)._check_identification_number()
    
    
