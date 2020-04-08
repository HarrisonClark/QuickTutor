
from django import forms
from study.models import Student
from study.models import Tutor

class EditProfile(forms.Form):
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    student_year = forms.CharField(max_length=50, required=False)
    picture = forms.URLField(required=False)
    bio = forms.CharField(max_length=100, widget=forms.Textarea, required=False)