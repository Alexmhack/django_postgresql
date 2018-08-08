from django.urls import path

from .views import (
	BlogListView,
)

urlpatterns = [
	path('list/', views.BlogListView.as_view(), name='blog-list'),
]