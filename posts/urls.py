from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_feed, name='post_feed'),
    url(r'^(?P<pk>[0-9]+)/$', views.post_detail,name='post_detail'),
   # url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^like/$', views.post_like, name='like'),
    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),

]