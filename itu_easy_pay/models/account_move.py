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

    def action_register_itu_payment(self):
        ''' Open the account.payment.register wizard to pay the selected journal entries.
        :return: An action opening the account.payment.register wizard.
        '''
        return {
            'name': _('Register Payment'),
            'res_model': 'itu.easy_pay.itu_register',
            'view_mode': 'form',
            'context': {
                'active_model': 'account.move',
                'active_ids': self.ids,
            },
            'target': 'new',
            'type': 'ir.actions.act_window',
        }