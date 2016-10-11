from django.conf.urls import url 
from . import views

urlpatterns = [
    # url(r'^$', views.ListRacks.as_view(), name='rack_list'),
    url(r'^$', views.ClosestDist.as_view(), name='rack_list'),

]



