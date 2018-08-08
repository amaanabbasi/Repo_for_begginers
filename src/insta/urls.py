from django.conf.urls import url, include
from . import views

app_name = "insta"
urlpatterns = [
    url(r'user/',views.userdetail, name='userdetail'),
]


