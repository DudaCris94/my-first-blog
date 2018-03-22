from django.conf.urls import url, include 
from django.contrib.auth.decorators import login_required
from views import index_vehiculo, vehiculo_view, vehiculo_list, vehiculo_edit, vehiculo_delete



urlpatterns = [
    url(r'^inicio', login_required(index_vehiculo),name='inicio'),
    url(r'^registrar$', login_required(vehiculo_view),name='nuevo_vehiculo'),
    url(r'^listar$', login_required(vehiculo_list),name='listar_vehiculo'),
    url(r'^editar/(?P<id_vehiculo>\d+)$', login_required(vehiculo_edit),name='vehiculo_editar'),
    url(r'^eliminar/(?P<id_vehiculo>\d+)$', login_required(vehiculo_delete),name='vehiculo_eliminar'),
]
