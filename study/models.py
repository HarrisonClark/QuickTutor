from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class StudentRatings(models.Model):
    rating = models.IntegerField()
    comment = models.CharField(max_length=200)
    # student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # rater = models.ForeignKey(Rating)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    student_year = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    picture = models.URLField()
    bio = models.CharField(max_length=200)
    rating = models.ForeignKey(StudentRatings, on_delete=models.CASCADE)


