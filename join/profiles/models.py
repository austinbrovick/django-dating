from __future__ import unicode_literals
from django.conf import settings
from django.db import models
User = settings.AUTH_USER_MODEL

GENDERS = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

SEEKING = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Both', 'Both')
)


RACES = (
    ('White', 'White'),
    ('Black', 'Black'),
    ('Asian', 'Asian'),

)

PL = (
    ('Python', 'Python'),
    ('Java', 'Java'),
    ('PHP', 'PHP'),
    ('JavaScript', 'JavaScript'),
    ('C++', 'C++'),
    ('Swift', 'Swift'),
    ('Objective-C', 'Objective-C'),
    ('C', 'C')
)



def user_directory_path(instance, filename):
    print "******* in upload function *************"
    print instance
    print filename
    location = str(instance.user.username)
    return "%s/%s" %(location, filename)



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=15, choices=GENDERS)
    seeking = models.CharField(max_length=15, choices=SEEKING)
    github_username = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(blank=True)
    favorite_programming_language = models.CharField(max_length=50, blank=True, choices=PL)
    college = models.CharField(max_length=30, blank=True, null=True)
    current_title = models.CharField(max_length=30, blank=True, null=True)
    current_employer = models.CharField(max_length=50, blank=True, null=True)
    race = models.CharField(max_length=50, choices=RACES, blank=True)

    profile_picture = models.ImageField(upload_to=user_directory_path,
        null=True,
        blank=True,
        width_field="width_field",
        height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)


    def __unicode__(self):
        return self.user.username


class GithubInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.IntegerField(null=True)
    following = models.IntegerField(null=True)
    public_repos = models.IntegerField(null=True)
    html_url = models.URLField(max_length=100, null=True)

    def __unicode__(self):
        return self.user.username


