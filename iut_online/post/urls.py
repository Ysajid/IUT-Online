from django.conf.urls import *
import views

urlpatterns = [
    url(r'^comment/', views.comment, name="comment"),
]