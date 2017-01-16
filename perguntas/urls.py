from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^central/(?P<page>[0-9]+)/$', views.central, name = 'centralP'),
    url(r'^posicao/(?P<page>[0-9]+)/$', views.posicao, name = 'posicaoP'),
    url(r'^variancia/(?P<page>[0-9]+)/$', views.variancia, name = 'varianciaP'),
    url(r'^graficos/(?P<page>[0-9]+)/$', views.graficos, name = 'graficosP'),
    url(r'^regressao/(?P<page>[0-9]+)/$', views.regressao, name = 'regressaoP'),
]