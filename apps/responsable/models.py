# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.db import models

from apps.vehiculo.models import Vehiculo

# Create your models here.
class Responsable(models.Model):
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	cedula = models.IntegerField()
	cargo = models.CharField(max_length=50)
	vehiculo = models.OneToOneField(Vehiculo, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return '{}'.format(self.vehiculo.placa)

