from django.urls import re_path

from user import views

urlpatterns = [
    # re_path(r'^register/$', views.register),
    re_path(r'^register/$', views.RegisterView.as_view()),
    re_path(r'^login/$', views.login),
    re_path(r'^info/(?P<id>\d+)/$', views.view_info)
]