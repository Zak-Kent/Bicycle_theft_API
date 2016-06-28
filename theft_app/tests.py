from rest_framework.test import APITestCase
from django.core.urlresolvers import reverse
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory

from factories import BicycleParkingFactory
from . import models 
from . import serializers
from . import views 


# class ViewResponseTest(APITestCase): 

    # def test_object_creation(self): 
    #     self.test_obj = BicycleParkingFactory()

    #     self.assertEqual(self.test_obj.__unicode__(), self.test_obj.gid)
    #     self.assertEqual(self.test_obj.bilinear_score, 0.8812073629861754)
    #     self.assertTrue(isinstance(self.test_obj, models.BicycleParkingPdx))

    # def test_view_returns_json_response(self):
    #     self.test_obj = BicycleParkingFactory()
    #     self.test_obj.save()
    #     self.client = APIClient()

    #     url = reverse('theft_app:rack_list')
    #     self.assertEqual(url, '/api/v1/racks/'.decode('utf-8'))

    #     resp = self.client.get(url)
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertEqual(resp.content, '{}') 
        # still need to find a way to build a testing DB maybe test from 
        # DB itself with a unit test and don't test with Django test runner 

class UrlParamsTest(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()

    def tearDown(self):
        pass
    
    def test_get_user_lat_long(self):
        self.client = APIClient()
        url = reverse('theft_app:locate_racks', kwargs={'lati':5.555, 'longi':5.5555})
        self.assertEqual(url, '/api/v1/racks/5.555,5.5555')

        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, ('5.555', '5.5555'))

    def test_get_user_dist_lat_long(self): 
        pass







        
        
        








