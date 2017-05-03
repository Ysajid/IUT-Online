from django.conf.urls import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin

from iut_online.university.models import LoginForm
from iut_online.university import views
from iut_online.post import views as post_views
from iut_online.post import urls as post_urls
from iut_online.calender import views as calender_views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^hello/$', views.hello, name='hello'),
    url(r'^login/$', LoginView.as_view(template_name = 'login.html', authentication_form = LoginForm), name="login"),
    url(r'^register/$', views.register_user, name="register"),
    url(r'^logout/$', LogoutView.as_view(next_page = 'login') , name="logout"),
    url(r'^posts/([0-9]+)/', post_views.posts, name="posts"),
    url(r'^post/$', post_views.post, name="post"),
    url(r'^manage/', include(admin.site.urls) , name="manage"),
    url(r'^posts/', include(post_urls), name="post"),
    url(r'^calender/', calender_views.home, name="calendar")
]
