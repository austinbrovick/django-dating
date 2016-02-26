from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Chat(models.Model):
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	user = models.ForeignKey(User)
	message = models.CharField(max_length=200)