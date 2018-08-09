from django.shortcuts import render
from django.views import generic

from .models import Blog

from datetime import datetime
from datetime import timedelta

class BlogListView(generic.ListView):
	model = Blog

	def get_context_data(self, **kwargs):
		context = super(BlogListView, self).get_context_data(**kwargs)
		context['flight_list_view'] = Blog.objects.filter(
			published_date__lte=datetime.now() + timedelta(days=-3))[:5]
		return context


class BlogDetailView(generic.DetailView):
	model = Blog