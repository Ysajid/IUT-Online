from django.conf.urls import *
from django.contrib import admin
import university.urls

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'iut_online.views.home', name='home'),
    # url(r'^iut_online/', include('iut_online.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    #jet urls
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls), name="admin"),
    # url(r'^hello/', 'social.view.hello', name='hello'),
    url(r'^social/', include(university.urls)),
    url(r'^comments/', include('django_comments.urls')),

]
