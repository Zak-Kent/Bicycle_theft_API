from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
 
from .views import ListRacks

class ViewResponseTest(APITestCase):
    fixtures = ['fixtures/json_test.json', ]

    def test_get_api_json(self):
        factory = APIRequestFactory()
        view = ListRacks.as_view()

        request = factory.get('api/v1/racks/') 
        response = view(request)
        response.render()
        self.assertEqual(response.status_code, status.HTTP_200_OK)








