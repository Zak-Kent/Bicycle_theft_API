from rest_framework.views import APIView
from rest_framework.response import Response

from services import Location_info
from . import models
from . import serializers 


class ListRacks(APIView):
    def get(self, request, format=None):
        rack = models.BicycleParkingPdx.objects.all()
        serializer = serializers.BikeParkingSerializer(rack, many=True)
        return Response(serializer.data)


class LocateRacks(APIView):

    def get(self, request, format=None, **kwargs):
        self.lati = self.kwargs['lati']
        self.longi = self.kwargs['longi']
        self.dist = self.kwargs['disti']

        print "!" * 60 
        print self.dist, self.lati, self.longi
        print "!" * 60 

        location_service = Location_info(self.lati, self.longi, self.dist)

        racks = location_service.racks_within_distance()

        return Response(racks)

class LocateRacksDefault(APIView):

    def get(self, request, format=None, **kwargs):
        self.lati = self.kwargs['lati']
        self.longi = self.kwargs['longi']
        self.dist = 50

        print "!" * 60 
        print self.dist, self.lati, self.longi
        print "!" * 60 

        location_service = Location_info(self.lati, self.longi, self.dist)

        racks = location_service.racks_within_distance()

        return Response(racks)






#Zipcode.objects.filter(poly__distance_lte=(geom, D(m=5)))
