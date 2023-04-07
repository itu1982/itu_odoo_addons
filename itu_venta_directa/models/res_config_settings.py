from odoo import models, fields, api
import logging, random
from odoo.addons.itu_log.models import itu_log

ItuLog = itu_log.ItuLog()


class ItuVentaDirectaSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    ProductVD = fields.Many2one ('product.product', string='Product:', help='Product for Direct Sell', required=True)
    ProductTemplateVD = fields.Many2one ('product.template', string='Product template:', help='Product for Direct Sell', required=False)
    RememberOnlyVDPriceUnit = fields.Boolean (string='Remember only VD Price unit', help='In Sales, remember Price Unit only in VD Product when product quantity is changed', required=False, default=False)

   
    def set_values(self):
       """ Set itu repair values"""
       res = super(ItuVentaDirectaSettings, self).set_values()
       param = self.env['ir.config_parameter'].sudo()
       
       field1 = self.ProductVD and self.ProductVD.id or False
       field2 = self.ProductTemplateVD and self.ProductTemplateVD.id or False
       field3 = self.RememberOnlyVDPriceUnit or False

       param.set_param('itu.venta_directa.ProductVD', field1)
       param.set_param('itu.venta_directa.ProductTemplateVD', field2)
       param.set_param('itu.venta_directa.RememberOnlyVDPriceUnit', field3)

       return res
       
    def get_values(self):
        """Get itu repair values"""
        res = super(ItuVentaDirectaSettings, self).get_values()
        param = self.env['ir.config_parameter'].sudo()
        
        field1 = param.get_param('itu.venta_directa.ProductTemplateVD') or False
        field2 = param.get_param('itu.venta_directa.ProductVD') or False
        field3 = param.get_param('itu.venta_directa.RememberOnlyVDPriceUnit') or False

        
        res.update(
           ProductTemplateVD=int(field1)
        )
        res.update(
           ProductVD=int(field2)
        )
        res.update(
           RememberOnlyVDPriceUnit=field3
        )
        return res