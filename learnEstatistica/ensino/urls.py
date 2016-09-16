from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^central/(?P<page>[0-9]+)/$', views.central, name = 'central'),
    url(r'^posicao/(?P<page>[0-9]+)/$', views.posicao, name = 'posicao'),
    url(r'^variancia/(?P<page>[0-9]+)/$', views.variancia, name = 'variancia'),
    url(r'^graficos/(?P<page>[0-9]+)/$', views.graficos, name = 'graficos'),
    url(r'^regressao/(?P<page>[0-9]+)/$', views.regressao, name = 'regressao'),
]