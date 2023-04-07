from odoo import models,fields,api
from odoo.http import request
from datetime import datetime
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
from pprint import pprint
from odoo.addons.itu_log.models import itu_log
import logging, random

ItuLog = itu_log.ItuLog()

class VentaDirectaAccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    ## Esta opcion sirve serviria si queremos controlar las ventas directas al 
    ## crear la factura o presupuesto. 
    ## En un principio lo comento por que vamos a controlarlas al crear cada 
    ## linea de factura o presupuesto
    ##
    ##
    ##@api.model_create_multi
    ##def create(self, vals_list):
    ##    ItuLog.DebugText(" **************** VD CREATE ************** ")
    ##   temp_vals_list = []
    ##    for vals in vals_list:
    ##        if 'product_id' in vals and 'name' in vals:
    ##            ItuLog.DebugText(" VD = Existen los campos ")
    ##            ItuLog.DebugText(str(vals["product_id"]))
    ##            ItuLog.DebugText(str(vals["name"]))
    ##            ItuLog.DebugText(str(vals["account_id"]))
    ##            if vals["product_id"] == False and vals["name"] != False:
    ##                ItuLog.DebugText(" **************** VD CambiandoProductID ***************** ")
    ##                vals["product_id"] = 4
    ##                vals["account_id"] = 1125
    ##        temp_vals_list.append(vals) 
    ##            
    ##    rslt = super(VentaDirectaAccountMoveLine, self).create(temp_vals_list)
    ##    return rslt

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