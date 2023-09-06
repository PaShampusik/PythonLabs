from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import LoginForm, UserRegistrationForm


class AccountViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')


class AccountFormTest(TestCase):
    def test_login_form_valid(self):
        form = LoginForm(data={'username': 'testuser', 'password': 'testpassword'})
        self.assertTrue(form.is_valid())

    def test_login_form_invalid(self):
        form = LoginForm(data={'username': 'testuser', 'password': ''})
        self.assertFalse(form.is_valid())

    def test_user_registration_form_valid(self):
        form = UserRegistrationForm(data={
            'username': 'newuser',
            'first_name': 'John',
            'email': 'john@example.com',
            'password': 'newpassword',
            'password2': 'newpassword'
        })
        self.assertTrue(form.is_valid())
