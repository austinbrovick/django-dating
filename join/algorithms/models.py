from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from profiles.models import UserProfile

User = settings.AUTH_USER_MODEL

class Algo(models.Model):
    creator = models.OneToOneField(User, on_delete=models.CASCADE)
    algorithm = models.TextField()
    answer = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.algorithm

class PPLWhoHaveSolvedAlgo(models.Model):
    algo = models.ForeignKey(Algo, on_delete=models.CASCADE)
    solver = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.algo)
