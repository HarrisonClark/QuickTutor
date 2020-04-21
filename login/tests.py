from django.test import TestCase
import json
import uuid
from datetime import timedelta

from django import forms
from django.conf import settings
from django.contrib.auth.models import AbstractUser, AnonymousUser
from django.contrib.sites.models import Site
from django.core import mail, validators
from django.core.exceptions import ValidationError
from django.db import models
from django.http import HttpResponseRedirect
from django.template import Context, Template
from django.test.client import Client, RequestFactory
from django.test.utils import override_settings
from django.urls import reverse
from django.utils.timezone import now

from allauth.account.forms import BaseSignupForm, ResetPasswordForm, SignupForm
from allauth.account.models import (
    EmailAddress,
    EmailConfirmation,
    EmailConfirmationHMAC,
)
from allauth.tests import Mock, TestCase, patch
from allauth.utils import get_user_model, get_username_max_length

# Create your tests here.
class LoginTests(TestCase):

	def test_username(self):
		# Create user
		user = get_user_model().objects.create(username='testcase1')
		user.set_password('test1')
		user.save()
		EmailAddress.objects.create(user=user, email="testcase1@test.com", primary=True, verified=True)
		# Get response
		response = self.client.post(reverse('account_login'), {'login': 'testcase1', 'password': 'test1'})
		self.assertRedirects(response, settings.LOGIN_REDIRECT_URL, fetch_redirect_response=False)
		
	def test_username2(self):
		# Create user
		user = get_user_model().objects.create(username='testcase12')
		user.set_password('test1')
		user.save()
		EmailAddress.objects.create(user=user, email="testcase12@test.com", primary=True, verified=True)
		# Get response
		response = self.client.post(reverse('account_login'), {'login': 'testcase1', 'password': 'test1'})
		self.assertRedirects(response, settings.LOGIN_REDIRECT_URL, fetch_redirect_response=False)