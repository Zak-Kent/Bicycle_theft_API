from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers 


class ListRacks(APIView):
    def get(self, request, format=None):
        rack = models.BicycleParkingPdx.objects.get(gid=10)
        serializer = serializers.BikeParkingSerializer(rack)
        return Response(serializer.data)








#Zipcode.objects.filter(poly__distance_lte=(geom, D(m=5)))
