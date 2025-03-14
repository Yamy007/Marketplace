from rest_framework.test import APITestCase
from apps.user.serializers import UserModel
from django.urls import reverse
from rest_framework import status
from .models import MarketPlaceModel

class TestMarketplaceApi(APITestCase):

    def setUp(self):
        self.user = {
            "email": "test_1@gmail.com",
            "password": "2803",
            "profile": {
                "name": "Tester",
                "surname": "Test",
                "age": 20,
            }
        }
        self.marketplace = {
            'name':"Rozetka",
            'description':"Test M",
            'slogan':"First Test"
        }

    def _auth(self, admin=None, superuser=None):
        auth_req = {
            "email": self.user.get('email'),
            "password": self.user.get('password')
        }

        res = self.client.post(reverse('create_user'), self.user, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        user = UserModel.objects.get(email=self.user.get('email'))
        if admin:
            user.is_staff = True
        if superuser:
            user.is_superuser = True
        user.save()

        res = self.client.post(reverse('auth_login'), auth_req, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {res.data["access"]}')



    def test_create_marketplace(self):
        self._auth()
        res= self.client.post(reverse('create_marketplace'), self.marketplace, format='json')
        count = MarketPlaceModel.objects.count()
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(count, 1)
    

    def test_get_my_marketplace(self):
        self._auth()
        res = self.client.get(reverse('get_my_marketplace'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)


    