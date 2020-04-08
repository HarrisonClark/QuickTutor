from django.test import TestCase
from .forms import EditProfile
# Create your tests here.
class testEditProfileForm(TestCase):

    def editProfile_valid_form(self):
        form = EditProfile.objects.create(first_name = "Harshita", last_name = "Pathipati",student_year = "second")
        self.assertTrue(form.is_valid())

    def editProfile_valid_form2(self):
        form2 = EditProfile.objects.create(last_name = "Pathipati",student_year = "second")
        self.assertFalse(form2.is_valid())

