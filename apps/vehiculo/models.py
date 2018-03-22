# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.db import models



# Create your models here.
class Vehiculo(models.Model):
	placa = models.CharField(max_length=8)
	marca = models.CharField(max_length=50)
	tipo = models.CharField(max_length=50)
	color = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.placa)