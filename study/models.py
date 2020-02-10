from django.db import models

class StudentRatings(models.Model):
    rating = models.IntegerField()
    comment = models.CharField(max_length=200)
    # student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # rater = models.ForeignKey(Rating)

