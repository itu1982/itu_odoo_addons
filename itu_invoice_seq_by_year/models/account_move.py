from odoo import models,fields,api
from odoo.http import request
from datetime import datetime
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
from pprint import pprint
from odoo.addons.itu_log.models import itu_log
import logging, random

ItuLog = itu_log.ItuLog()

class ItuInvoiceSeqByYear(models.Model):
    _inherit = 'account.move'

    def _get_starting_sequence(self):
        if self.journal_id.journal_by_year:
            ItuLog.DebugText(" **************** GET SEQ BY YEAR ENABLE ************** ")
            self.ensure_one()
            starting_sequence = "%s/%04d/0000" % (self.journal_id.code, self.date.year)
            if self.journal_id.refund_sequence and self.move_type in ('out_refund', 'in_refund'):
                starting_sequence = "R" + starting_sequence
            return starting_sequence
        else:
            ItuLog.DebugText(" **************** GET SEQ BY YEAR DISABLE ************** ")
            result = super(ItuInvoiceSeqByYear, self)._get_starting_sequence()
            return result