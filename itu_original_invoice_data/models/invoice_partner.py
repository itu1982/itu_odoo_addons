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

class ItuInvoicePartner (models.Model):
    _name = 'itu.invoice.partner'
    _description = 'Invoice Partner data'
    name = fields.Char('Name: ', copy=False, readonly=True, index=True)
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char(change_default=True)
    city = fields.Char()
    state = fields.Char()
    country = fields.Char()
    vat = fields.Char(string='Tax ID', index=True, help="The Tax Identification Number. Complete it if the contact is subjected to government taxes. Used in some legal statements.")
    email = fields.Char()