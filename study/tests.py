from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import StudentRatings, Student

class TestStudentRatings(TestCase):
    def setUp(self):
        StudentRatings.objects.create(rating=5, comment="Excellent!")
    def test_specific_rating(self):
        stu_comment = StudentRatings.objects.get(comment="Excellence")
        self.assertEqual(stu_comment.review_sentence(), 'This student has a rating of 5, and a student said \"excellent\" about this tutor')