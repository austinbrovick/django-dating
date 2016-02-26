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






  # if form.is_valid():
  #   instance = form.save(commit=False)
  #   instance.creator = request.user
  #   instance.save()
  #   return redirect("my_profile")
