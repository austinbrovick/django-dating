from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.conf import settings

def index(request):


	info = {
		'Name': 'Name',
	}
	return render(request, 'home/index.html', {'STATIC_URL': settings.STATIC_URL, 'info': info})