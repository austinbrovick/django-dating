from __future__ import unicode_literals

from django.db import models

from profiles.models import UserProfile

class Match(models.Model):
    one = models.BooleanField(default=False)
    two = models.BooleanField(default=False)
