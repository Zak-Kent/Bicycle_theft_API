from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.gis.geos import *
from django.contrib.gis.measure import D

from . import models
from . import serializers 


class ListRacks(APIView):
    def get(self, request, format=None):
        rack = models.BicycleParkingPdx.objects.all()
        serializer = serializers.BikeParkingSerializer(rack)
        return Response(serializer.data)


class LocateRacks(APIView):
    model = models.BicycleParkingPdx


    def get(self, request, format=None, **kwargs):
        self.lati = float(self.kwargs['lati'])
        self.longi = float(self.kwargs['longi'])
        self.dist = self.kwargs.get('dist', '100')

        self.point = GEOSGeometry('Point({} {})'.format(self.lati, self.longi), srid=4326)

        self.test = models.BicycleParkingPdx.objects.filter(geom__distance_lt=(self.point, self.dist))
        #self.test = models.BicycleParkingPdx.objects.get(gid=10)
        serializer = serializers.BikeParkingSerializer(self.test)

        return Response(serializer.data)






#Zipcode.objects.filter(poly__distance_lte=(geom, D(m=5)))
