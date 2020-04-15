from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.contrib.postgres.fields import ArrayField


class StudentRatings(models.Model):
    rating = models.IntegerField()
    comment = models.CharField(max_length=200)
    # student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # rater = models.ForeignKey(Rating)

    # return 'Rating is {}, and comment is \" {} \"'.format(self.rating, self.comment)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_year = models.CharField(max_length=50)
    picture = models.URLField()
    bio = models.TextField(max_length=100, blank=True)
    # CoursesTaken = ArrayField(
    #     models.ForeignKey(Course, on_delete=models.CASCADE), blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Course(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    subject = models.CharField(max_length=4)
    course_number = models.CharField(max_length=4)

    def __str__(self):
        return self.subject + self.course_number


class tutorRequest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    tutor = models.ForeignKey(
        Student, on_delete=models.CASCADE, blank=True, related_name="requestTutor", null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.course.subject + self.course.course_number + ": " + self.description


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        new_student = Student(user=instance)
        new_student.save()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.student.save()
