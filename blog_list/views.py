from django.shortcuts import render
from django.views import generic

from .models import Blog

class BlogListView(generic.ListView):
	model = Blog


class BlogDetailView(generic.DetailView):
	model = Blog