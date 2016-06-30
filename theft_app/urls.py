from django.conf.urls import url 
from . import views


# bug in regex that matches dist value with supplied dist 

urlpatterns = [
    url(r'^$', views.ListRacks.as_view(), name='rack_list'),
    url(r'^(?P<lati>-?([1-8]?[1-9]|[1-9]0)\.{1}\d{1,6}),(?P<longi>-?([1]?[1-7][1-9]|[1]?[1-8][0]|[1-9]?[0-9])\.{1}\d{1,6}$)', 
        views.LocateRacksDefault.as_view(), name='locate_racks'),
    url(r'^(?P<disti>^\d+)/(?P<lati>-?([1-8]?[1-9]|[1-9]0)\.{1}\d{1,6}),(?P<longi>-?([1]?[1-7][1-9]|[1]?[1-8][0]|[1-9]?[0-9])\.{1}\d{1,6}$)', 
        views.LocateRacks.as_view(), name='locate_default'),
]



