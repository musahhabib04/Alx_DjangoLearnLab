from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post

class PostCrudTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u', password='p')
        self.post = Post.objects.create(title='T', content='C', author=self.user)

    def test_post_list(self):
        resp = self.client.get(reverse('post-list'))
        self.assertEqual(resp.status_code, 200)

    def test_create_requires_login(self):
        resp = self.client.get(reverse('post-create'))
        self.assertRedirects(resp, '/login/?next=' + reverse('post-create'))


# Create your tests here.
