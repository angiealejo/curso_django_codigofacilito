from django.conf.urls import url

from apps.usuario.views import RegistroUsuario

urlpatterns = [
	url(r'^registrar', RegistroUsuario.as_view(), name="registrar")

]
