from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Algo, PPLWhoHaveSolvedAlgo
from profiles.models import UserProfile
from .forms import AlgoForm

User = get_user_model()

# Create your views here.
def create_algo_page(request):
  algo_form = get_object_or_404(Algo, creator=request.user)
  form = AlgoForm(instance=algo_form)
  context = {
    "form" : form,
  }
  return render(request, 'algorithms/create_algo_page.html', context)


def create_algo(request):
  my_algo, created = Algo.objects.get_or_create(creator=request.user)
  form = AlgoForm(request.POST or None, instance=my_algo)
  if form.is_valid():
    instance = form.save(commit=False)
    instance.creator = request.user
    instance.save()
    return redirect("my_profile")
  context = {
    "form" : form
  }
  return render(request, 'algorithms/create_algo_page.html', context)



def solve_algo(request, username):
  prospect = User.objects.get(username=username)
  algorithm = Algo.objects.get(creator=prospect)
  print algorithm.creator.username
  context = {
    "algorithm" : algorithm,
  }
  return render(request, "algorithms/algorithm.html", context)
  return HttpResponse("fuck yes!!!!")

def check_answer(request, creator):
  solver = UserProfile.objects.get(user=request.user)
  creator_obj = User.objects.get(username=creator)
  algo = Algo.objects.get(creator=creator_obj)
  guess = request.POST.get('guess')
  if guess == algo.answer:
    PPLWhoHaveSolvedAlgo.objects.create(algo=algo, solver=solver)
    user_profile = User.objects.get(username=creator)
    me = request.user
    algo_creator = User.objects.get(username=creator)
    algo_solver = UserProfile.objects.get(user=me)
    view_status = PPLWhoHaveSolvedAlgo.objects.filter(algo__creator=algo_creator, solver=algo_solver)
    print view_status
    if view_status:
        status = True
    else:
        status = False
    print status

    context = {
        "prospect" : creator_obj,
        "status" : status,
    }
    return render(request, 'matches/prospect_profile.html', context)


  else:
    return HttpResponse("fuck yes!!!!")





  # if form.is_valid():
  #   instance = form.save(commit=False)
  #   instance.creator = request.user
  #   instance.save()
  #   return redirect("my_profile")
