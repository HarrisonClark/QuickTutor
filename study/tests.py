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

  
class StudentRatingsTestCase(TestCase):

    def setUp(self):
        StudentRatings.objects.create(rating = 5, comment = "helpful")
        StudentRatings.objects.create(rating = 1, comment = "rude")
    
    def test_number_of_ratings(self):
        self.assertEquals(StudentRatings.objects.all().count(),2)

    def test_rating(self):
        five = StudentRatings.objects.get(rating = 5)
        self.assertEqual(five.rating, 5)
