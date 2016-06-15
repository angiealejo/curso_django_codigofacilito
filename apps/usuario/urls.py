from django.conf.urls import url

from apps.usuario.views import RegistroUsuario, UserAPI

urlpatterns = [
	url(r'^registrar', RegistroUsuario.as_view(), name="registrar"),
	url(r'^api', UserAPI.as_view(), name="api"),

]
