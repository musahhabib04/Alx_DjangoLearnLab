from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from .models import Post

User = get_user_model()

class PostTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser','t@t.com','pass1234')
        self.client.force_authenticate(user=self.user)

    def test_create_post(self):
        url = reverse('post-list')
        data = {'title':'Test','content':'body'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)

# Create your tests here.
