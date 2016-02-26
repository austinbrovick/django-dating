from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model # so we can get the User object
from django.contrib.auth.decorators import login_required

from .forms import UserProfileForm
from .models import UserProfile, GithubInfo

import requests
import json


from django.apps import apps
Algo = apps.get_app_config('algorithms').models['algo']

User = get_user_model() # getting the current user as the User Object




@login_required
def profile(request):
    me = get_object_or_404(User, id=request.user.id)
    my_profile_info, created = UserProfile.objects.get_or_create(user=me)
    my_algo, created = Algo.objects.get_or_create(creator=request.user)
    github, created = GithubInfo.objects.get_or_create(user=request.user)

    context = {
        "user" : my_profile_info,
    }
    return render(request, "profiles/my_profile.html", context)

@login_required
def edit_profile_page(request):
    user_form = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=user_form)
    context = {
        "user" : request.user,
        "form" : form,
    }
    return render(request, "profiles/edit_profile.html", context)

@login_required
def edit_profile(request):
    my_profile_info, created = UserProfile.objects.get_or_create(user=request.user)
    github, created = GithubInfo.objects.get_or_create(user=request.user)

    print my_profile_info.github_username

    if my_profile_info.github_username != "":
        jsonList = []
        req =requests.get('https://api.github.com/users/'+ str(my_profile_info.github_username))
        print req
        jsonList.append(json.loads(req.content))
        print jsonList
        parsedData = []
        userData = {}
        if jsonList[0]:
            userData['html_url'] = jsonList[0]['html_url']
            userData['followers'] = jsonList[0]['followers']
            userData['following'] = jsonList[0]['following']
            userData['blog'] = jsonList[0]['blog']
            userData['email'] = jsonList[0]['email']
            userData['public_gists'] = jsonList[0]['public_gists']
            userData['public_repos'] = jsonList[0]['public_repos']
            userData['avatar_url'] = jsonList[0]['avatar_url']
            parsedData.append(userData)

        gh_info = GithubInfo.objects.get(user=request.user)
        print gh_info
        gh_info.html_url = userData['html_url']
        gh_info.followers = userData['followers']
        gh_info.following = userData['following']
        gh_info.public_repos = userData['public_repos']

        gh_info.save()


    form = UserProfileForm(request.POST or None, request.FILES or None, instance=my_profile_info)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect("my_profile")

    context = {
        "form" : form,
    }
    return render(request, "profiles/edit_profile.html", context)





    # get profile info and render profile
    # me = get_object_or_404(User, id=request.user.id)
    # my_profile_info, created = UserProfile.objects.get_or_create(user=me)
    # context = {
    #     "user" : my_profile_info,
    # }
    # return render(request, "profiles/my_profile.html", context)



    # user_info, created = UserProfile.objects.get_or_create(user=request.user)
    # form = UserProfileForm(request.POST or None, request.FILES or None, instance=user_info)
    # if form.is_valid():
    #     instance = form.save(commit=False)
