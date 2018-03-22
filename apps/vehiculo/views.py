# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from forms import VehiculoForm, VehiculoForm2
from models import Vehiculo


# Create your views here.
def index_vehiculo(request):
	vehiculo = Vehiculo.objects.all().order_by('id')
	contexto = {'vehiculos':vehiculo}
	return render(request, 'vehiculo/index.html', contexto)

def vehiculo_view(request):
	if request.method == 'POST':
		form = VehiculoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('vehiculo:listar_vehiculo')
	else:
		form = VehiculoForm()

	return render(request, 'vehiculo/vehiculo_form.html', {'form':form})

def vehiculo_list(request): 
	vehiculo = Vehiculo.objects.all().order_by('id')
	contexto = {'vehiculos':vehiculo}
	return render(request, 'vehiculo/vehiculo_list.html', contexto)


def vehiculo_edit(request, id_vehiculo):
	vehiculo = Vehiculo.objects.get(id=id_vehiculo)
	if request.method == 'GET':
		form = VehiculoForm2(instance=vehiculo)
	else:
		form = VehiculoForm(request.POST, instance=vehiculo)
		if form.is_valid():
			form.save()
		return redirect ('vehiculo:listar_vehiculo')
	return render(request, 'vehiculo/vehiculo_form2.html', {'form':form,'vehiculo':vehiculo})

def vehiculo_delete(request, id_vehiculo):
	vehiculo = Vehiculo.objects.get(id=id_vehiculo)
	if request.method == 'POST':
		vehiculo.delete()
		return redirect ('vehiculo:listar_vehiculo')
	return render(request, 'vehiculo/vehiculo_delete.html', {'vehiculo':vehiculo})

