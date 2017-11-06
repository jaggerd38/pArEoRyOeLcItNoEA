from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.vuelo_index, name="vuelo_index"),
    url(r'^vuelo/(?P<pk>[0-9]+)/$', views.detalle_vuelo, name='ver_vuelo'),
    url(r'^vuelo/nuevo/$', views.vuelo_nuevo, name='vuelo_nuevo'),
    url(r'^vuelo/(?P<pk>[0-9]+)/editar/$', views.vuelo_editar, name='vuelo_editar'),


    url(r'^avion/$', views.avion_index, name="avion_index"),
    url(r'^avion/(?P<pk>[0-9]+)/$', views.detalle_avion, name='ver_avion'),
    url(r'^avion/nuevo/$', views.avion_nuevo, name='avion_nuevo'),
    url(r'^avion/(?P<pk>[0-9]+)/editar/$', views.avion_editar, name='avion_editar'),

    url(r'^pasajero/$', views.pasajero_index, name="pasajero_index"),
    url(r'^pasajero/nuevo/$', views.pasajero_nuevo, name='pasajero_nuevo'),
    url(r'^pasajero/(?P<pk>[0-9]+)/$', views.detalle_pasajero, name='ver_pasajero'),
    url(r'^pasajero/(?P<pk>[0-9]+)/editar/$', views.pasajero_editar, name='pasajero_editar'),

    url(r'^boleto/$', views.boleto_index, name="boleto_index"),
    url(r'^boleto/nuevo/$', views.boleto_nuevo, name='boleto_nuevo'),
    url(r'^boleto/(?P<pk>[0-9]+)/$', views.detalle_boleto, name='ver_boleto'),
    url(r'^boleto/(?P<pk>[0-9]+)/editar/$', views.boleto_editar, name='boleto_editar'),
]
