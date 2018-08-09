from django.urls import path

from .views import (
	BlogListView,
	BlogDetailView,
)

urlpatterns = [
	path('', BlogListView.as_view(), name='blog-list'),
	path('blog/<int:pk>/detail', BlogDetailView.as_view(), name='blog-detail'),
]