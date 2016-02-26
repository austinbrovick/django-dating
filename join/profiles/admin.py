from django.contrib import admin



from .models import UserProfile, GithubInfo

admin.site.register(UserProfile)

admin.site.register(GithubInfo)
