from django.db import models
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.contrib.auth.models import User
from study.models import Student


@receiver(user_signed_up)
def saveProfilePic(request, user, **kwargs):
    try:
        user.student.picture = user.socialaccount.extra_data['picture']
        user.save()
    except:
        print("Picture couldn't be saved")
