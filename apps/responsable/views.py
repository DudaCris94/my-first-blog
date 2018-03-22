# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from forms import ResponsableForm, ResponsableForm2
from models import Responsable

# Create your views here.
def index_responsable(request):
	return render(request, 'responsable/index.html')

def responsable_view(request):
	if request.method == 'POST':
		form = ResponsableForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('responsable:index_responsable')
	else:
		form = ResponsableForm()

	return render(request, 'responsable/responsable_form.html', {'form':form})

def responsable_list(request):
	responsable = Responsable.objects.all()
	contexto = {'responsables':responsable}
	return render(request, 'responsable/responsable_list.html', contexto)

	

#Vistas basadas en clases

class ResponsableList(ListView):
	model = Responsable
	template_name = 'responsable/responsable_list.html'
	
class ResponsableCreate(CreateView):
	model = Responsable
	form_class = ResponsableForm
	template_name = 'responsable/responsable_form.html'
	success_url = reverse_lazy('responsable:listado_responsables')

class ResponsableUpdate(UpdateView):
	model = Responsable
	form_class = ResponsableForm2
	template_name = 'responsable/responsable_form2.html'
	success_url = reverse_lazy('responsable:listado_responsables')

class ResponsableDelete(DeleteView):
	model = Responsable
	template_name = 'responsable/responsable_delete.html'
	success_url = reverse_lazy('responsable:listado_responsables')