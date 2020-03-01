from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db.models.signals import post_save
from django.dispatch import receiver

class StudentRatings(models.Model):
    rating = models.IntegerField()
    comment = models.CharField(max_length=200)
    # student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # rater = models.ForeignKey(Rating)

        # return 'Rating is {}, and comment is \" {} \"'.format(self.rating, self.comment)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    student_year = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    picture = models.URLField()
    bio = models.CharField(max_length=200, blank = True)
    rating = models.ForeignKey(StudentRatings, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        new_student = Student(user=instance)
        new_student.save()

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.student.save()