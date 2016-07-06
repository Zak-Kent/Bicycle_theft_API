# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
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


    def __unicode__(self):
        return (self.gid) 


class TheftGrid(models.Model):
    geom = models.GeometryField(srid=srid)
    num_racks = models.IntegerField(blank=True, null=True)
    num_corners = models.IntegerField(blank=True, null=True)
    num_thefts = models.IntegerField(blank=True, null=True)
    grid_score = models.DecimalField(max_digits=12, decimal_places=8, blank=True, null=True)
    point_geom = models.GeometryField(srid=srid)
    test_geom = models.GeometryField(srid=srid)
    valid_data = models.IntegerField(blank=True, null=True)
    degx = models.FloatField(blank=True, null=True)
    degy = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'theft_grid'

    def save(self, *args, **kwargs):
     return

    def delete(self, *args, **kwargs):
         return
