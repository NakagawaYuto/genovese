from django.urls import path
from .views import TestView

app_name = 'nutrients'

urlpatterns = [
    path('test/',  TestView.as_view(), name='test')
]
