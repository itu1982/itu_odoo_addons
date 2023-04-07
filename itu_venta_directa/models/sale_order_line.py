from odoo import models,fields,api
from odoo.http import request
from datetime import datetime
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
from pprint import pprint
from odoo.addons.itu_log.models import itu_log
import logging, random

ItuLog = itu_log.ItuLog()

class VentaDirectaSaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('name')
    def _VDOnChangeName(self):
        """Get itu repair settings values"""
        ItuLog.DebugText(str(self.product_id))
        
        if not self.product_id and self.display_type == False:
            ItuLog.DebugText('Product id no asignado')
            param = self.env['ir.config_parameter'].sudo()
            
            ProductTemplateVD = int(param.get_param('itu.venta_directa.ProductTemplateVD')) or False
            ProductVD = int (param.get_param('itu.venta_directa.ProductVD')) or False
            
            
            Producto = self.env['product.product'].search([('id', '=', ProductVD)], limit=1, order="id desc")   
            
            self.product_id = ProductVD
            if 'product_uom' in self and not self.product_uom:
                self.product_uom = Producto.uom_id
            
            if 'taxes_id' in self and not self.tax_id: 
                self.tax_id = Producto.taxes_id

        return {}
        
    @api.onchange('product_uom', 'product_uom_qty')
    def product_uom_change(self):
        
        #Recogemos el producto de venta directa.
        param = self.env['ir.config_parameter'].sudo()
        ProductVD = int (param.get_param('itu.venta_directa.ProductVD')) or False
        RememberOnlyVDPriceUnit = param.get_param('itu.venta_directa.RememberOnlyVDPriceUnit')
        
        #Si es el producto de venta directa guardamos el precio y luego se lo volvemos a poner
        #Si el producto no es VD pero RememberOnlyVDPriceUnit es False, guardamos el precio y luego se lo volvemos a poner 
        #Si RememberOnlyVDPriceUnit True y el producto no es VD, dejamos que el programa siga su curso normal.
           
        if RememberOnlyVDPriceUnit == False or self.product_id.id == ProductVD: 
            PriceUnit = self.price_unit
            res = super(VentaDirectaSaleOrderLine, self).product_uom_change()
            self.price_unit = PriceUnit
            ItuLog.DebugText('Volvemos a poner el precio: ' + str(self.price_unit))
        else:
            res = super(VentaDirectaSaleOrderLine, self).product_uom_change()