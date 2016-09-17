from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.home, name = 'home1'),
    url(r'^reset/$',views.reset, name = 'reset')
]
