# from django.shortcuts import render
from django.views import generic

# Create your views here.

class TestView(generic.TemplateView):
    template_name = 'test.html'
