from rest_framework_gis.filters import DistanceToPointFilter
from rest_framework import generics

from . import models
from . import serializers 

class ListRacks(generics.ListAPIView):
    queryset = models.BicycleParkingPdx.objects.all()
    serializer_class = serializers.BikeParkingSerializer
    distance_filter_field = 'geom'
    filter_backends = (DistanceToPointFilter, )
    distance_filter_convert_meters = True



