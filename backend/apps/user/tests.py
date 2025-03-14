from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from apps.user.serializers import UserModel


class TestUserApi(APITestCase):
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

    def test_create(self):
        count_before = UserModel.objects.count()
        res = self.client.post(reverse('create_user'), self.user, format='json')
        count_after = UserModel.objects.count()

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(count_after, count_before + 1)

    def test_list_user(self):
        res = self.client.get(reverse('list_user'))
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_user_admin(self):
        self._auth(admin=True)
        res = self.client.get(reverse('list_user'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_me(self):
        self._auth()
        res = self.client.get(reverse('get_me'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
