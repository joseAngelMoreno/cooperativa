# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class prodcuto_model(models.Model):
    _name = 'cooperativa.producto_model'
    _description = 'Modelo de productos'
    _sql_constraints = [
        ("id_socio_nombreUnico","UNIQUE (name)","No puede haber dos productos con el mismo nombre!!"),]

    
    
   
    name=fields.Char(string="Nombre",required=True)
    descripcion=fields.Char(string="Descripcion",required=True)
    precio=fields.Float(string="Precio",required=True)
    kilosTotales=fields.Float(string="KiloTotales",default=0,readonly=True)
    campanya_id2=fields.One2many("cooperativa.campanya_model","producto_id",string="campanya")




    def ponerCero(self):
        self.kilosTotales=0



    @api.constrains("precio")
    def precioNegativo(self):
    
        if self.precio<0:
            raise ValidationError("Precio no puede ser negativo")
       
            
    