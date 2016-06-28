from django.conf.urls import url 
from . import views


# bug in regex that matches dist value with supplied dist 

urlpatterns = [
    url(r'^$', views.ListRacks.as_view(), name='rack_list'),
    url(r'^(?P<lati>(\-?\d+(\.\d+)?)),(?P<longi>(\-?\d+(\.\d+)?))', views.LocateRacksDefault.as_view()),
    url(r'^(?P<disti>^\d+)/(?P<lati>(\-?\d+(\.\d+)?)),(?P<longi>(\-?\d+(\.\d+)?))', views.LocateRacks.as_view()),
]



