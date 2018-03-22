from django.conf.urls import url, include 
from django.contrib.auth.decorators import login_required

from views import index_responsable, responsable_view, responsable_list, \
	ResponsableList, ResponsableCreate, ResponsableUpdate, ResponsableDelete

urlpatterns = [
    url(r'^$', login_required(index_responsable),name='index_responsable'),
    url(r'^registrar$', login_required(ResponsableCreate.as_view()),name='nuevo_responsable'),
    url(r'^listado$', login_required(ResponsableList.as_view()),name='listado_responsables'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(ResponsableUpdate.as_view()),name='editar_responsables'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(ResponsableDelete.as_view()),name='eliminar_responsable'),

]
