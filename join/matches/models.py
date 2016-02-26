from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile

class Match(models.Model):

    match_status = models.BooleanField(default=False)
    one = models.ForeignKey(UserProfile, related_name="matchone", on_delete=models.CASCADE)
    two = models.ForeignKey(UserProfile, related_name="matchtwo", on_delete=models.CASCADE)
    oneLikesTwo = models.BooleanField(default=False)
    twoLikesOne = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)
