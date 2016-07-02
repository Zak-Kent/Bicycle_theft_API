from rest_framework.views import APIView
from rest_framework.response import Response

from services import Location_info
from . import models
from . import serializers 

#------------------------------------------------------------------
from rest_framework_gis.filters import DistanceToPointFilter
from rest_framework import generics


class ListRacks(generics.ListAPIView):
    queryset = models.BicycleParkingPdx.objects.all()
    serializer_class = serializers.BikeParkingSerializer
    distance_filter_field = 'geom'
    filter_backends = (DistanceToPointFilter, )
    distance_filter_convert_meters = True

class LocateRacks(APIView):

    def get(self, request, format=None, **kwargs):
        self.lati = self.kwargs['lati']
        self.longi = self.kwargs['longi']
        self.dist = self.kwargs['disti']

        location_service = Location_info(self.lati, self.longi, self.dist)

        racks = location_service.racks_within_distance()

        return Response(racks)

class LocateRacksDefault(APIView):

    def get(self, request, format=None, **kwargs):
        self.lati = self.kwargs['lati']
        self.longi = self.kwargs['longi']
        self.dist = 50

        location_service = Location_info(self.lati, self.longi, self.dist)

        racks = location_service.racks_within_distance()

        return Response(racks)

