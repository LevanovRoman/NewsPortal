from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


class MainPage(ListView):
    model = Post
    template_name = 'main-page.html'


class ShowPost(DetailView):
    model = Post
    template_name = 'post-page.html'


class Category(ListView):
    ...





