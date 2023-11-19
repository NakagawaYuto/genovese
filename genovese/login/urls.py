from django.contrib import admin
from django.urls import path
from login.views import frontpage, post_detail, Login, Logout

app_name = 'login'

urlpatterns = [
    path("", frontpage, name="home"),
    path("<slug:slug>/", post_detail, name="post_detail"),

    #login
    path('login', Login.Login.as_view(), name="login"),

    #logout
    path('logout', Logout.Logout.as_view(), name="logout"),
]
