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
    # url(r'^robots\.txt/$', views.robots),
    # url(r'^robots\.txt/$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),


]
# u(r'^robots\.txt/$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),




urlpatterns += staticfiles_urlpatterns()
