from django.test import TestCase

# Create your tests here.

"""
factory = APIRequestFactory()
request = factory.post(url, post data)
"""

"""from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

from polls import apiviews"""

# class TestPoll(APITestCase):

#     def setUp(self):
#         self.factory = APIRequestFactory()
#         self.view = apiviews.PollViewSet.as_view({'get': "list"})
#         self.url = '/polls/'

#     def test_list(self):
#         request = self.factory.get(self.uri)
#         response = self.view(request)
#         self.assertEqual(response.status_code, 200, 'Expected Response Code 200, recieved {0} instead. '.format(response.status_code))

"""from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from polls import apiviews"""

# class TestPoll(APITestCase):
#     def setUp(self):
#         self.factory = APIRequestFactory()
#         self.view = apiviews.PollViewSet.as_view({'get': "list"})
#         self.url = '/polls/'
#         self.user = self.setup_user()
#         self.token = Token.objects.create(user=self.user)
#         self.token.save()

#     @staticmethod
#     def setup_user():
#         User = get_user_model()
#         return User.objects.create_user(
#                 'test', 
#                 email="testuser@test.com", 
#                 password="test"
#         )
#     def test_list(self):
#         request = self.factory.get(self.url, HTTP_AUTHORIZATION="Token {}".format(self.token.key))
#         request.user = self.user
#         response = self.view(request)
#         self.assertEqual(response.status_code, 200, 'Expected Response Code 200, recieved {0} instead.'.format(response.status_code))


from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from polls import apiviews
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

class TestPoll(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.view = apiviews.PollViewSet.as_view({'get': "list"})
        self.uri = '/polls/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
                'test', 
                email="testuser@test.com", 
                password="test"
        )

    def test_list2(self):
        self.client.login(username="test", password="test")
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200, 'Expected Response Code 200, recieved {0} instead.'.format(response.status_code))

    def test_create(self):
        self.client.login(username="test", password="test")
        params = {
            "question": "How are you?",
            "created_by": 1
            }
        response = self.client.post(self.uri, params)
        self.assertEqual(response.status_code, 201, "Expected Response Code 201, recieved {0} instead.".format(response.status_code))

        
