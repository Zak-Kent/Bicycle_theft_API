from django.contrib.gis.db import models

srid = 4326

class BicycleParkingPdx(models.Model):
    gid = models.AutoField(primary_key=True)
    degx = models.FloatField(blank=True, null=True)
    degy = models.FloatField(blank=True, null=True)
    geom = models.GeometryField(srid=srid)
    bilinear_score = models.DecimalField(max_digits=12, decimal_places=8, blank=True, null=True)
    objects = models.GeoManager() 

    class Meta:
        managed = False
        db_table = 'bicycle_parking_pdx'

    def save(self, *args, **kwargs):
        return

    def delete(self, *args, **kwargs):
        return

