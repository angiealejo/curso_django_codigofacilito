from django.conf.urls import url, include

from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, \
	MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', MascotaCreate.as_view(), name='mascota_crear'),
    url(r'^listar$', MascotaList.as_view(), name='mascota_listar'),
    url(r'^editar/(?P<pk>\d+)/$', MascotaUpdate.as_view(), name='mascota_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', MascotaDelete.as_view(), name='mascota_eliminar'),

]
