from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user
from django.urls import reverse
from django.http import HttpRequest

from .models import TSUser


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        pass

    def test_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        pass


class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            'userlogin', 'test@email.com', 'password')
        self.tsuser = TSUser.objects.create(user=self.user, major=TSUser.INFORMATICS, role=TSUser.STALLKEEPER)

    def test_login_logout(self):
        response = self.client.post(reverse('login'), {'username': 'userlogin', 'password': 'password'}, follow=True)
        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)
        self.assertRedirects(response, reverse('dashboard'))
        
        response = self.client.get(reverse('logout'))
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)
        self.assertRedirects(response, '/')


    def test_login_invalid(self):
        response = self.client.post(reverse('login'), {'username': 'falseuser', 'password': 'falsepassword'}, follow=True)
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)
        self.assertEquals(response.request['PATH_INFO'], '/login/')