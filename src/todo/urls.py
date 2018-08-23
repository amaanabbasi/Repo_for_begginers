from django.conf.urls import url, include
from . import views, apis

app_name='todo'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/v1/get/', apis.read, name='read'),
    url(r'^api/v1/add/$', apis.create, name='create'),
    url(r'^api/v1/update/(?P<todoID>\d+)/$', apis.update, name='update'),
    url(r'^api/v1/delete/(?P<todoID>\d+)/$', apis.delete, name='delete'),
]
