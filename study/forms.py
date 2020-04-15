from django import forms
from .models import Course


class TutorRequestForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    description = forms.CharField()


class ClaimRequestForm(forms.Form):
    pass
