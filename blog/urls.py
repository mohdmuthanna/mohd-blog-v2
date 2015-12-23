from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views


urlpatterns = [
    url(r'^b/', include('db.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^a/$', include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'^cv/$', views.cv),
    url(r'^smedia/$', views.smedia),
    url(r'^contact/$', views.contact),

]

urlpatterns += staticfiles_urlpatterns()
