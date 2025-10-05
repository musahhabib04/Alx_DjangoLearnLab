# blog/tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment

class CommentTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='author', password='pass')
        self.other = User.objects.create_user(username='other', password='pass')
        self.post = Post.objects.create(title='T', content='C', author=self.user)
        self.comment = Comment.objects.create(post=self.post, author=self.user, content='hello')

    def test_comment_visible_on_post_detail(self):
        resp = self.client.get(reverse('post-detail', args=[self.post.pk]))
        self.assertContains(resp, 'hello')

    def test_create_comment_requires_login(self):
        url = reverse('comment-create', args=[self.post.pk])
        resp = self.client.post(url, {'content': 'new comment'})
        # not logged in should redirect to login
        self.assertEqual(resp.status_code, 302)
        self.client.login(username='other', password='pass')
        resp2 = self.client.post(url, {'content': 'new comment'}, follow=True)
        self.assertEqual(resp2.status_code, 200)
        self.assertContains(resp2, 'new comment')

    def test_edit_comment_by_author(self):
        edit_url = reverse('comment-update', args=[self.comment.pk])
        # other user cannot edit
        self.client.login(username='other', password='pass')
        resp = self.client.get(edit_url)
        self.assertEqual(resp.status_code, 403)  # or redirect depending on mixin settings

        # author can edit
        self.client.login(username='author', password='pass')
        resp2 = self.client.post(edit_url, {'content': 'edited'}, follow=True)
        self.assertEqual(resp2.status_code, 200)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, 'edited')

    def test_delete_comment_by_author(self):
        del_url = reverse('comment-delete', args=[self.comment.pk])
        self.client.login(username='author', password='pass')
        resp = self.client.post(del_url, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(Comment.objects.filter(pk=self.comment.pk).exists())
