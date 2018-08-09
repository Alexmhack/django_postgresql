from django.shortcuts import render
from django.views import generic

from .models import Blog

from datetime import datetime
from datetime import timedelta

class BlogListView(generic.ListView):
	model = Blog

	def get_context_data(self, **kwargs):
		context = super(BlogListView, self).get_context_data(**kwargs)
		context['latest_list'] = Blog.objects.filter(
			published_date__gte=datetime.now() - timedelta(days=3))[:5]
		return context


class BlogDetailView(generic.DetailView):
	model = Blog