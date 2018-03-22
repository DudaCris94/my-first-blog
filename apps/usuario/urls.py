from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from views import RegistroUsuario

urlpatterns = [
	url(r'^registrarUsuario',RegistroUsuario.as_view(), name="registrar"),
]