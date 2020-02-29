from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import StudentRatings, Student

class TestStudentRatings(TestCase):
    def setUp(self):
        StudentRatings.objects.create(rating=5, comment="Excellent!")
    def test_specific_rating(self):
        stu_comment = StudentRatings.objects.get(rating=5, comment="Excellent").first()
        self.assertEqual(stu_comment.review_sentence(), 'Rating is ' + str(5) + " and the comment is " + "\"Excellent!\"")
