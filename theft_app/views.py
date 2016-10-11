from rest_framework_gis.filters import DistanceToPointFilter
from rest_framework import generics

from django.contrib.gis.geos import Point
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers 

class ListRacks(generics.ListAPIView):
    """
    This endpoint lists all racks in the database with their ids, longitude(degx), latitude(degy),
    and theft score. 

    To search for racks within given distance you must pass in a query string 
    with a distance in which you want to search and a point which is a set of coordinates
    in lon,lat format.

    eg: api/v1/racks/?dist=50&point=-122.678713,45.514798

    Which is equivalant to filtering within 50 meters of the point (-122.678713,45.514798). 

    """
    queryset = models.BicycleParkingPdx.objects.all()
    serializer_class = serializers.BikeParkingSerializer
    distance_filter_field = 'geom'
    filter_backends = (DistanceToPointFilter, )
    distance_filter_convert_meters = True

# ----------------------------------------------------------------------


class ClosestDist(generics.ListAPIView):
    """Endpoint takes lat/long cords and returns  """
    serializer_class = serializers.BikeParkingSerializer

    def get_queryset(self):
        point = self.get_filter_point(self.request)
        # dist = request.query_params.get('dist', None)

        bike_racks = models.BicycleParkingPdx.objects.distance(point).order_by('distance')[:30]

        return bike_racks

    def get_filter_point(self, request):
        """grab point out of query string and make a geos point"""
        point_param = 'point'
        point_string = request.query_params.get(point_param, None)
        
        if not point_string:
            return None

        try:
            (x, y) = (float(n) for n in point_string.split(','))
        except ValueError:
            raise ParseError('Invalid geometry string supplied for parameter {0}'.format(self.point_param))

        point_string = Point(x, y, 4326)    

        return point_string

  




