from django.conf.urls import url
from . import views


urlpatterns = [
  url(r'^$', views.prospects, name='prospects'),
  url(r'^prospect/(?P<username>\w+)/$', views.prospect_profile, name='prospect_profile'),
]


# url(r'^$', views.ProfileView.as_view()),
    # # url(r'^(?P<username>\w+)/$', views.profile),
    # # url(r'^(?P<username>\w+)/add_info/$', views.add_user_info_page, name='add_user_info_page'),
    # # url(r'^(?P<username>\w+)/add_info/response/$', views.add_user_info, name='add_user_info'),

    # url(r'^$', views.profile),

    # url(r'^$', views.my_profile, name='my_profile'),
    # url(r'^edit_profile_page/', views.edit_profile_page, name='edit_profile_page'),
    # url(r'^edit_profile/', views.edit_profile, name='edit_profile'),
    # # url(r'^edit_profile_info_page/', views.edit_profile_info_page, name='edit_profile_info_page'),
    # # url(r'^prospect_profile/(?P<id>\d+)$', views.prospect_profile, name='prospect_profile'),

