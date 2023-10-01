from django.contrib import admin
from django.urls import path

app_name = 'login'

urlpatterns = [
    path('admin/', admin.site.urls),
]
