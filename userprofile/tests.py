from django.test import TestCase
from .forms import EditProfile
# Create your tests here.

from django.test import TestCase
from django.test import Client
from .forms import *   # import all forms


class testEditProfileForm(TestCase):

    def test_editProfile_valid_form(self):
        form = EditProfile(data={
            'first_name': "Harshita", 'last_Name': "Pathipati", 'student_year': '2022', 'bio': "", 'picture': ""
        })
        self.assertFalse(form.is_valid())

    def test_editProfile_valid_form2(self):
        form2 = EditProfile(data={
            'first_name': "Harshita", 'last_Name': "", 'student_year': 2022, 'bio': "", 'picture': ""
        })
        self.assertFalse(form2.is_valid())
