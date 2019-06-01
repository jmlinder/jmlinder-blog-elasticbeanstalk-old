from django.test import RequestFactory
from django.urls import reverse
#from django.contrib.auth.models import User, AnonymousUser
from blog.views import *
from mixer.backend.django import mixer
from django.test import TestCase
import pytest


@pytest.mark.django_db
class TestViews(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestViews, cls).setUpClass()
        mixer.blend('blog.Post')
        cls.factory = RequestFactory()

    # Post list page / Home
    def test_post_list(self):
        path = reverse('post_list')
        request = self.factory.get(path)
        response = post_list(request)
        assert response.status_code == 200

    # Post detail page
    def test_post_detail(self):
        path = reverse('post_detail', kwargs={'pk': 1})
        request = self.factory.get(path)
        response = post_detail(request, pk=1)
        assert response.status_code == 200

    # Post edit page
    def test_post_edit_authenticated(self):
        path = reverse('post_edit', kwargs={'pk': 1})
        request = self.factory.get(path)
        request.user = mixer.blend(User)
        response = post_edit(request, pk=1)
        assert response.status_code == 200

    def test_post_edit_unauthenticated(self):
        path = reverse('post_edit', kwargs={'pk': 1})
        request = self.factory.post(path)
        request.user = AnonymousUser()
        response = post_edit(request, pk=1)
        assert 'accounts/login' in response.url and response.status_code == 302

    # New post page
    def test_post_new_authenticated(self):
        path = reverse('post_new')
        request = self.factory.get(path)
        request.user = mixer.blend(User)
        response = post_new(request)
        assert response.status_code == 200

    def test_post_new_unauthenticated(self):
        path = reverse('post_new')
        request = self.factory.get(path)
        request.user = AnonymousUser()
        response = post_new(request)
        assert 'accounts/login' in response.url and response.status_code == 302

    # Drafts page
    def test_post_draft_list_authenticated(self):
        path = reverse('post_draft_list')
        request = self.factory.get(path)
        request.user = mixer.blend(User)
        response = post_draft_list(request)
        assert response.status_code == 200

    def test_post_draft_list_unauthenticated(self):
        path = reverse('post_draft_list')
        request = self.factory.get(path)
        request.user = AnonymousUser()
        response = post_draft_list(request)
        assert 'accounts/login' in response.url and response.status_code == 302

    # Publish page
    def test_post_publish_authenticated(self):
        path = reverse('post_publish', kwargs={'pk': 1})
        request = self.factory.post(path)
        request.user = mixer.blend(User)
        response = post_publish(request, pk=1)
        assert '/post/1' in response.url

    def test_post_publish_unauthenticated(self):
        path = reverse('post_publish', kwargs={'pk': 1})
        request = self.factory.post(path)
        request.user = AnonymousUser()
        response = post_publish(request, pk=1)
        assert 'accounts/login' in response.url and response.status_code == 302

    # Delete page
    def test_post_remove_authenticated(self):
        path = reverse('post_remove', kwargs={'pk': 1})
        request = self.factory.post(path)
        request.user = mixer.blend(User)
        response = post_remove(request, pk=1)
        assert '/' in response.url and response.status_code == 302

    def test_post_remove_unauthenticated(self):
        path = reverse('post_remove', kwargs={'pk': 1})
        request = self.factory.post(path)
        request.user = AnonymousUser()
        response = post_remove(request, pk=1)
        assert 'accounts/login' in response.url

    # About page
    def test_about(self):
        path = reverse('about')
        request = self.factory.get(path)
        response = about(request)
        assert response.status_code == 200

    # Projects page
    def test_projects(self):
        path = reverse('projects')
        request = self.factory.get(path)
        response = projects(request)
        assert response.status_code == 200
