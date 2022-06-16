#-*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.http import request
from datetime import datetime
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
from pprint import pprint
from odoo.addons.itu_log.models import itu_log
import logging, random

ItuLog = itu_log.ItuLog()

class payment_itu_register(models.Model):
    _name = 'itu.payment.itu_register'
    _inherit = 'account.payment.register'
    _description = 'Extension of Payments Windows'
       
    invoice_datetime2 = fields.Datetime('Invoice Date')
    received_money = fields.Monetary('Received Money')
    # == Fields given through the context ==
    line_ids = fields.Many2many('account.move.line', 'account_payment_itu_register_move_line_rel', 'wizard_id', 'line_id',
        string="Journal items", readonly=True, copy=False,)