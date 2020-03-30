
from django import forms
from study.models import Student
from django.contrib.auth.forms import UserChangeForm

class EditProfile(UserChangeForm):

    class Meta:
        model = Student
        fields = (
            'first_name',
            'last_name',
            'student_year',
            'bio'
        )