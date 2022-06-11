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
    journal_by_year = fields.Boolean('Sequences by year', help='Enable Invoice sequence only by Code and Year. Only Works for new sequences. e.g. Fact/2022/0001', default=1)
