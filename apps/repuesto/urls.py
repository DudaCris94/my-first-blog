from django.conf.urls import url, include 
from django.contrib.auth.decorators import login_required
from views import index_repuesto, repuesto_view, repuesto_list, search, reporte, fechas, reporteFiltrado, imprimir,   \
	RepuestoList, RepuestoCreate, RepuestoUpdate, RepuestoDelete, Reporte, ReportePDF


urlpatterns = [
    url(r'^$', login_required(index_repuesto),name='index_repuesto'),
    url(r'^nuevo$', login_required(RepuestoCreate.as_view()),name='nuevo_repuesto'),
    url(r'^lista', login_required(RepuestoList.as_view()),name='lista_repuestos'),
    url(r'^reporte', login_required(reporte),name='reporte'),
    url(r'^filtrado/$', login_required(fechas),name='reporte_filtrado'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(RepuestoUpdate.as_view()),name='editar_repuestos'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(RepuestoDelete.as_view()),name='eliminar_repuestos'),
    url(r'^buscar/$', login_required(search),name='buscar'),
    
    url(r'^imprimir/(?P<query>[^/]+)/(?P<query2>[^/]+)/(?P<query3>[^/]+)/$', login_required(imprimir),name='imprimir'),



]