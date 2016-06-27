from django.conf.urls import url 
from . import views


# bug in regex that matches dist value with supplied dist 

urlpatterns = [
    url(r'^$', views.ListRacks.as_view(), name='rack_list'),
    url(r'^(?P<lati>(\-?\d+(\.\d+)?)),(?P<longi>\s*(\-?\d+(\.\d+)?)/(?P<dist>[1-9]\d*$))', views.LocateRacks.as_view(), name='locate_racks'),
    url(r'^(?P<lati>(\-?\d+(\.\d+)?)),(?P<longi>\s*(\-?\d+(\.\d+)?))', views.LocateRacks.as_view()),
]



