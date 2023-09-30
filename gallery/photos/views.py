from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.
class HomeView(ListView):
    model = get_user_model()
    template_name = 'index.html'
