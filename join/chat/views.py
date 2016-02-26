from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

from .models import Chat
from .forms import ChatForm
from django.contrib.auth.models import User

@login_required
def groupchat(request):
	current_user = request.user
	chat = Chat.objects.all()
	form = ChatForm(request.POST or None)

	if request.method == "POST":
		holder = request.POST.get("user")
		user = User.objects.get(id=holder)

		message = request.POST.get("message")
		created = request.POST.get("created")

		Chat.objects.create(user=user, message=message, created=created)
		form = ChatForm()

	context= {
		'current_user': current_user,
		'form': form,
		'chat': chat,
	}

	return render(request, 'chat/groupchat.html', context)

@login_required
def Message(request):
	c = Chat.objects.all()
	return render(request, 'chat/messages.html', {'chat': c})