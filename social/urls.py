from django.conf.urls import *
from django.contrib.auth.views import LoginView, LogoutView
from social.models import LoginForm
from social import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'hello/$', views.hello, name='hello'),
    url(r'login/$', LoginView.as_view(template_name = 'login.html', authentication_form = LoginForm), name="login"),
    url(r'register/$', views.register_user, name="register"),
    url(r'logout/$', LogoutView.as_view(next_page = 'home') , name="logout"),
    url(r'post', views.post, name="post")
]
