from . import models 
from rest_framework import serializers 
from rest_framework_gis import serializers as gis_serializer 


class BikeParkingSerializer(gis_serializer.GeoModelSerializer):
    class Meta:
        fields = (
            'gid',
            'degx',
            'degy',
            'bilinear_score',
            )
        model = models.BicycleParkingPdx
        geo_field = 'geom'