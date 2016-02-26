from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.apps import apps

from django.contrib.auth.models import User

UserProfile = apps.get_app_config('profiles').models['userprofile']

# Create your views here.
def prospects(request):
    my_profile = UserProfile.objects.get(user=request.user)
    my_gender = my_profile.gender
    seeking = my_profile.seeking

    prospects = UserProfile.objects.filter(seeking=my_gender, gender=seeking)

    context = {
        "prospects" : prospects,
    }
    return render(request, 'matches/prospects.html', context)


def prospect_profile(request, username):
    user = User.objects.get(username=username)
    print user
    print user.githubinfo.html_url
    context = {
        "prospect" : user,
    }
    return render(request, 'matches/prospect_profile.html', context)
