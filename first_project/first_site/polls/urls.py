from django.conf.urls import url

from . import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^v2/', views.view2, name='bla')
]
