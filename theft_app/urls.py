from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.ListRacks.as_view(), name='rack_list'),
    url(r'^(?P<lati>(\-?\d+(\.\d+)?)),(?P<longi>\s*(\-?\d+(\.\d+)?)$)', views.LocateRacks.as_view(), name='locate_racks'),
]



