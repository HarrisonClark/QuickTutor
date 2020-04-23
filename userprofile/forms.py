
from django import forms
from study.models import Student


class EditProfile(forms.Form):
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    # student_year = forms.CharField(max_length=50, required=False)
    student_year = forms.ChoiceField(choices=[(x, x) for x in range(1, 5)])
    picture = forms.URLField(
        required=False, help_text="Paste URL of desired picture")
    bio = forms.CharField(max_length=200, widget=forms.Textarea(
        attrs={"rows": 5, "cols": 20}), required=False)
