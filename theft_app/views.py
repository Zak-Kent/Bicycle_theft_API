from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers 


class ListRacks(APIView):
    def get(self, request, format=None):
        rack = models.BicycleParkingPdx.objects.all()
        serializer = serializers.BikeParkingSerializer(rack)
        return Response(serializer.data)


class LocateRacks(APIView):
    def get(self, request, **kwargs):
        self.lati = self.kwargs['lati']
        self.longi = self.kwargs['longi']

        return Response((self.lati, self.longi))






#Zipcode.objects.filter(poly__distance_lte=(geom, D(m=5)))
