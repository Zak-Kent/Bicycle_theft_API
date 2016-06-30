from django.db import connections 

import logging

class Location_info:
    """take users lat/long and create an object that has methods to return their interpolated score and a list of 
        bicycle racks and their scores within a given distance""" 

    def __init__(self, lati, longi, dist):
        self.lati = lati
        self.longi = longi
        self.dist = dist 

        self.cursor = self.db_connect()

    def db_connect(self):
        try:
            self.cur = connections['legacy'].cursor()
            return self.cur
        except:
            logging.debug("I am unable to connect to the database")

    def racks_within_distance(self):
        """find all racks within provied dist value and return their lat/long, and theft_score"""

        sql_state = """SELECT degx, degy, bilinear_score 
        FROM bicycle_parking_pdx
        WHERE ST_Distance(ST_GeomFromText(%s)::geography, bicycle_parking_pdx.geom::geography) <= %s;"""

        point = 'POINT({} {})'.format(self.longi, self.lati)

        sql_data = [point, self.dist]
        self.cursor.execute(sql_state, sql_data)

        # makes JSON like dictionary object by hand due to issues with getting data from legacy DB/serializers 
        desc = self.cursor.description
        racks = {"racks" : [dict(zip([col[0] for col in desc], row)) for row in self.cursor.fetchall()]}

        return racks


logging.basicConfig(format='%(levelname)s %(funcName)s %(lineno)d:%(message)s', level=logging.DEBUG)