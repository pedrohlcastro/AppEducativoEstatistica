from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.menu, name = 'menu'),
	url(r'^credits/$',views.credits, name = 'credits'),
    url(r'^menu/$',views.home, name = 'home1'),
    url(r'^reset/$',views.reset, name = 'reset')
]
