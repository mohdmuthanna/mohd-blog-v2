from django.conf.urls import patterns, url
from . import views


urlpatterns = [
    # url(r'page/$', views.posts_list, {'category': 'all'}),

    url(r'^projects/page/(?P<page_no>\d+)/$', views.posts_list, {'category': 'project'}, name='project'),
    url(r'^projects/$', views.posts_list, {'category': 'project',},),

    url(r'^en/page/(?P<page_no>\d+)/$', views.posts_list, {'category': 'blog'}, name='blog'),
    url(r'^en/$', views.posts_list, {'category': 'blog'},),

    url(r'^ar/page/(?P<page_no>\d+)/$', views.posts_list, {'category': 'arabic'}, name='arabic'),
    url(r'^ar/$', views.posts_list, {'category': 'arabic'},),

    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post'),

    url(r'^page/(?P<page_no>\d+)/$', views.posts_list, {'category': 'all'}, name='all',),
    url(r'^page/$', views.posts_list, {'category': 'all'}),
    url(r'^$', views.posts_list, {'category': 'all'}),
]
    # url(r'^projects/', include('db.urls')),
    # url(r'^blog/', include('db.urls')),
    # url(r'^arabic/', include('db.urls')),
    # url(r'(?P<pk>\d+)/$', views.post_detail, name='post'),


# category = '??'
#
# a = category
#
# if category == 'blog':
#     a = 'blog'
# elif category == 'omar':
#     a = 'omar'
# elif category == 'page':
#     a = 'page'
# elif category == 'ali':
#     a = 'ali'
