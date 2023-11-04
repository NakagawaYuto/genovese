from django.contrib import admin
from django.urls import path

from login.views import frontpage, post_detail

app_name = 'login'

urlpatterns = [
    path("", frontpage, name="home"),
    path("<slug:slug>/", post_detail, name="post_detail")
]
