from django.conf.urls import url

from apps.adopcion.views import index_adopcion

urlpatterns = [
    url(r'^index$', index_adopcion)
]