#-*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.http import request
from datetime import datetime
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
from pprint import pprint
import logging, random

_logger = logging.getLogger(__name__)

class ItuLog():
    
    def DebugText(self, Mensaje):
        if self.debug_mode:
            _logger.critical(Mensaje)
        return {}

    def debug_mode(self):
        return request.session.debug