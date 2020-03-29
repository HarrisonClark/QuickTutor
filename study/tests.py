from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import StudentRatings, Student


class TutorRequestTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username="harrisonc", password="clark6789")

    def test_number_of_users(self):
        self.assertEqual(User.objects.all().count(), 1)
