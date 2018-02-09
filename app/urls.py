from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^teams_list/$', views.teams_list, name='teams_list'),
]