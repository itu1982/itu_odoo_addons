from odoo import models,fields,api
from odoo.http import request
from datetime import datetime
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
from pprint import pprint
from odoo.addons.itu_log.models import itu_log
import logging, random

ItuLog = itu_log.ItuLog()

class TbaiCompanyFS(models.Model):
    _inherit = "res.company"
    
    #aeat_fs_currency = fields.Many2one ('res.currency', string='Tbai fs Currency') 
    #aeat_fs_limit = fields.Monetary ('Simple invoice limit', currency_field='aeat_fs_currency')
    tbai_fs_limit = fields.Monetary ('Simple invoice limit')
    tbai_fs_journal_id = fields.Many2one ('account.journal', string='Account journal for Simple invoices') 