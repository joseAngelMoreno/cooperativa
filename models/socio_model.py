# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime,date
from odoo.exceptions import ValidationError
import re

class socio_model(models.Model):
    _name = 'cooperativa.socio_model'
    _description = 'Modelo de socios'
    _sql_constraints = [
        ("dni_dniUnico","UNIQUE (dni)","DNI ya esta en uso!!"),]
    _sql_constraints = [
        ("id_socio_socioUnico","UNIQUE (id_socio)","ID ya en uso!!"),]
    
    id_socio=fields.Integer(string="IdSocio",required=True)
    foto=fields.Binary(string="Foto")
    name=fields.Char(string="Nombre",required=True)
    apellidos=fields.Char(string="Apellidos",required=True)
    dni=fields.Char(string="Dni",required=True)
    fechaAlta=fields.Date(string="FechaAlta",default=date.today(),required=True)
    telefono=fields.Char(string="Tlfn",required=True,size=9)
    email=fields.Char(string="Email",required=True)
    saldo=fields.Float(string="Saldo",default=0)
    campanya_id=fields.One2many("cooperativa.campanya_model","socio_id",string="campanya")


    @api.constrains("email")
    def es_correo_valido(self):
        expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        comprueba= re.match(expresion_regular, self.email) is not None
        if comprueba==False:
            raise ValidationError("Formato de correo no valido")




    @api.constrains("dni")
    def _validacionDNI(self):
        
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        letra = self.dni[-1]
        num = self.dni[:-1]
        posi = int(num) % 23
        
        if letra != letras[posi]:
            raise ValidationError("DNI no valido")