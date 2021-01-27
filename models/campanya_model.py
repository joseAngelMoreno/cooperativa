# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class campanya_model(models.Model):
    _name = 'cooperativa.campanya_model'
    _description = 'Modelo de campanya'


    fecha=fields.Date(string="Fecha",default=datetime.today())
    campanya=fields.Char(string="Campaña",default=datetime.today().year)
    socio_id=fields.Many2one("cooperativa.socio_model","socio")
    producto_id=fields.Many2one("cooperativa.producto_model","producto")
    cantidad=fields.Float(string="Kilos")




    @api.constrains("cantidad")
    def menorDeCero(self):
    
        if self.cantidad<1:
            raise ValidationError("Cantidad debe ser mayor de 0")