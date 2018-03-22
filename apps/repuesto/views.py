# -*- coding: utf-8 -*-
from __future__ import absolute_import
from datetime import *

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.repuesto.forms import RepuestoForm, RepuestoForm2
from apps.repuesto.models import Repuesto
from apps.responsable.models import Responsable
from django.db.models import Q
from django.shortcuts import render_to_response

from django.http import HttpResponse
from django.views.generic import View
from apps.repuesto.render_to_pdf import render_to_pdf

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template


from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View



# Vistas basadas en funciones.

def index_repuesto(request):
	return render(request, 'repuesto/index.html')

def repuesto_view(request):
	if request.method == 'POST':
		form = RepuestoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('repuesto:index_repuesto')
	else:
		form = RepuestoForm()

	return render(request, 'repuesto/repuesto_form.html', {'form':form})

def repuesto_list(request):
	repuesto = Repuesto.objects.all()
	contexto = {'repuestos':repuesto }
	return render(request, 'repuesto/repuesto_list.html', contexto)

#Vistas basadas en clases

class RepuestoList(ListView):
	model = Repuesto
	template_name = 'repuesto/repuesto_list.html'
	paginate_by = 10
	
class RepuestoCreate(CreateView):
	model = Repuesto
	form_class = RepuestoForm
	template_name = 'repuesto/repuesto_form.html'
	success_url = reverse_lazy('repuesto:lista_repuestos')

class RepuestoUpdate(UpdateView):
	model = Repuesto
	form_class = RepuestoForm2
	template_name = 'repuesto/repuesto_form2.html'
	success_url = reverse_lazy('repuesto:lista_repuestos')

class RepuestoDelete(DeleteView):
	model = Repuesto
	template_name = 'repuesto/repuesto_delete.html'
	success_url = reverse_lazy('repuesto:lista_repuestos')

#def buscador(request, campo, texto):
    # ...
    # El campo dentro del filter debe ser el que fue mandado como parametro
    #resultado = Repuesto.objects.filter(campo__icontains=texto)
    #return render(request, 'repuesto/repuesto_list.html', resultado)

def buscador(request, texto):
	resultado = Repuesto.objects.filter(detalle__icontains= texto)
	return render(request, 'repuesto/repuesto_buscar.html', {'resultado': resultado})

class Reporte(ListView):
	model = Repuesto
	template_name = 'repuesto/reporte.html'
	paginate_by = 5
	
#def reporte(request):
#	responsable = Responsable.objects.all()
#	for i in responsable:
#		repuesto = Repuesto.objects.filter(responsable=i)
#		contexto = {'repuestos':repuesto}

#	return render(request, 'repuesto/reporte.html', contexto)


def reporte(request):
	responsable = Responsable.objects.all()
	repuesto = Repuesto.objects.all()
	#total=0
	#if repuesto:
	#	for x in repuesto:
	#		total=total+x.precio

	contexto = {'responsables': responsable, 'repuestos': repuesto}
	return render(request, 'repuesto/reporte.html', contexto)
	

def reporteFiltrado(request):
	responsable = Responsable.objects.all()
	repuesto = Repuesto.objects.filter(fechaCambio__range=('2018-02-01','2018-02-28'))
	#total=0
	#if repuesto:
	#	for x in repuesto:
	#		total=total+x.precio

	contexto = {'responsables': responsable, 'repuestos': repuesto}
	return render(request, 'repuesto/reporte.html', contexto)



def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(detalle__icontains=query) |
            Q(orden__icontains=query) |
            Q(adquisicion__icontains=query) |
            Q(responsable__nombre__icontains=query) |
            Q(responsable__apellidos__icontains=query) |
            Q(responsable__vehiculo__placa__icontains=query) 
        )
        results = Repuesto.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("repuesto/repuesto_buscar.html", {
        "results": results,
        "query": query
        
    })


def fechas(request):
    query = request.GET.get('q', '')
    query2 = request.GET.get('p', '')
    query3 = request.GET.get('r', '')
    total=0

    if query and query2:
        qset = (

           
            Q(fechaCambio__range=(query,query2), adquisicion__icontains= query3)
           
        )
       
        repuesto = Repuesto.objects.filter(qset).distinct()
        for x in repuesto:
        	total=total+x.precio
    else:
        repuesto = []
        responsable = []
    
    return render_to_response("repuesto/reporte.html", {
       
        "repuestos": repuesto,
        "query": query,
        "query2": query2,
        "query3": query3,
        "total":total

    })


def imprimir(request,query=None,query2=None,query3=None):
   
    total=0

    if query and query2:
        qset = (

           
            Q(fechaCambio__range=(query,query2), adquisicion__icontains= query3)
           
        )
       
        repuesto = Repuesto.objects.filter(qset).distinct()
        for x in repuesto:
            total=total+x.precio
    else:
        repuesto = []
        responsable = []
    
    return render(request, "repuesto/reporte2.html", {
       
        "repuestos": repuesto,
        "query": query,
        "query2": query2,
        "query3": query3,
        "total":total

    })



   


class ReportePDF(View):  
     
    def cabecera(self,pdf):
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = settings.MEDIA_ROOT+'/imagenes/logo.jpg'
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 40, 720, 120, 90,preserveAspectRatio=True)
        #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 8)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(210, 790, u"ESCUELA DE CAPACITACIÓN DE CONDUCTORES NO PROFESIONALES")
        pdf.setFont("Helvetica", 8)
        pdf.drawString(295, 780, u"SPORTMANCAR CIA. LTDA.")
        pdf.setFont("Helvetica", 8)
        pdf.drawString(305, 770, u"RUC: 1191721124001") 
        pdf.setFont("Helvetica", 8)
        pdf.drawString(165, 760, u"DIRECCIÓN: RAMON PINTO E/. VENEZUELA Y JOSE PICOITA. SECTOR PERPETUO SOCORRO")
        pdf.setFont("Helvetica", 8)
        pdf.drawString(300, 750, u"TELÉFONO: 072583139")
        pdf.setFont("Helvetica", 8)
        pdf.drawString(260, 740, u"EMAIL: SPORTMANCARLOJA@HOTMAIL.COM")  
        pdf.setFont("Helvetica", 8)
        pdf.drawString(310, 730, u"LOJA - ECUADOR")
        pdf.setFont("Helvetica", 8)
        pdf.drawString(65, 720, u"________________________________________________________________________________________________________")               

    def tabla( self,pdf,y):
        #Creamos una tupla de encabezados para neustra tabla
        encabezados = ('DNI', 'Nombre', 'Apellido Paterno', 'Apellido Materno')
        #Creamos una lista de tuplas que van a contener a las personas
        detalles = [(repuesto.detalle, repuesto.precio, repuesto.kilometraje, repuesto.responsable.nombre) for repuesto in Repuesto.objects.all()]
        #Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + detalles, colWidths=[2 * cm, 5 * cm, 5 * cm, 5 * cm])
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(3,0),'CENTER'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla 
        detalle_orden.wrapOn(pdf, 800, 600)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 60,y)

    def get(self, request, *args, **kwargs):
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        y = 600
        self.tabla(pdf, y)
        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response



