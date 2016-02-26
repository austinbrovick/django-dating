from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^groupchat/?', views.groupchat, name='chat_groupchat'),
    url(r'^messages/?', views.Message, name='chat_messages'),
]
