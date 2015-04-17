from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^serie/(?P<serie_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^serie/(?P<serie_id>[0-9]+)/saison/(?P<saison_id>[0-9]+)/$', views.detail_saison, name='saison'),
]