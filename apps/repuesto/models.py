# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.db import models

from apps.responsable.models import Responsable


# Create your models here.
class Repuesto(models.Model):

	CONVENIO = (
		('CASAKORE','CASAKORE'),
		('CULQUIMOTORS','CULQUIMOTORS'),
		('REP. MACAS','REP. MACAS'), 
		('P Y M', 'P Y M'),
		('LLANTAS','LLANTAS'),
		('COMPRAS EN EFECTIVO DE CARRO','COMPRAS EN EFECTIVO DE CARRO'),
		('COMPRAS EN EFECTIVO DE MOTO','COMPRAS EN EFECTIVO DE MOTO'),
	)


	detalle = models.CharField(max_length=50)
	orden = models.IntegerField()
	precio = models.DecimalField(max_digits=5, decimal_places=2)
	duracion = models.IntegerField(null=True)
	adquisicion = models.CharField(max_length=50, choices=CONVENIO, blank=False)
	fecha = models.DateField(null=True)
	fechaCambio = models.DateField(null=True)
	responsable = models.ForeignKey(Responsable, null=True, blank=True, on_delete=models.CASCADE)
	kilometraje = models.IntegerField()

	

