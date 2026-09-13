from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class AccountsTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_signup_and_profile_signal(self):
        signup_data = {
            'username': 'athlete_sam',
            'first_name': 'Sam',
            'last_name': 'Kerr',
            'email': 'sam@sportify.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!'
        }
        response = self.client.post(reverse('signup'), signup_data)
        self.assertEqual(response.status_code, 302)

        user = User.objects.get(username='athlete_sam')
        self.assertIsNotNone(user)
        self.assertIsNotNone(user.profile)

    def test_profile_requires_login(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)
