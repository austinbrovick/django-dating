from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.apps import apps

from django.contrib.auth.models import User
from .models import Match

UserProfile = apps.get_app_config('profiles').models['userprofile']
Algo = apps.get_app_config('algorithms').models['algo']
PPLWhoHaveSolvedAlgo = apps.get_app_config('algorithms').models['pplwhohavesolvedalgo']


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
    me = request.user

    algo_creator = User.objects.get(username=username)
    algo_solver = UserProfile.objects.get(user=me)

    view_status = PPLWhoHaveSolvedAlgo.objects.filter(algo__creator=algo_creator, solver=algo_solver)
    print view_status
    if view_status:
        status = True
    else:
        status = False
    print status

    context = {
        "prospect" : user,
        "status" : status,
    }
    return render(request, 'matches/prospect_profile.html', context)


def match_prospect(request, username):
    prospect = User.objects.get(username=username)
    prospect_userprofile = UserProfile.objects.get(user=prospect)

    me = User.objects.get(username=request.user)
    my_userprofile = UserProfile.objects.get(user=me)

    potential_match = Match.objects.filter(two=my_userprofile, one=prospect_userprofile)
    print potential_match
    if potential_match:
        print "there is a potential match"
        potential_match[0].match_status = True
        potential_match[0].twoLikesOne =True
        potential_match[0].save()
    else:
        match = Match(one=my_userprofile, two=prospect_userprofile, oneLikesTwo=True) # it will be false until the other person also matches me
        # if match.oneLikesTwo == True and match.twoLikesOne == True:
        #     match.match_status = True
        match.save()


    print username
    return redirect("prospects")


def my_matches(request):
    my_profile = UserProfile.objects.get(user=request.user)
    matches1 = Match.objects.filter(one=my_profile, match_status=True)
    matches2 = Match.objects.filter(two=my_profile, match_status=True)

    context = {
        "matches1" : matches1,
        "matches2" : matches2,
        "user" : request.user,

    }
    return render(request, "matches/my_matches.html", context)












