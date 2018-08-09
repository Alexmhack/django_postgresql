from django.db import models
from django.urls import reverse

from datetime import datetime, timedelta

class Blog(models.Model):
	title = models.CharField(max_length=50, help_text="Title for our blog", unique_for_date="published_date")
	content = models.TextField(help_text="Content for our blog")
	created_date = models.DateTimeField(auto_now_add=True, help_text="Date on which the blog is made")
	published_date = models.DateField(help_text="Default blog publish date of 5 days later", verbose_name="Published Date", default=datetime.now() + timedelta(days=5))
	edited_date = models.DateField(auto_now=True)

	def __str__(self):
		return f"Blog: {self.title}"

	def get_absolute_url(self):
		return reverse("blog-detail", args=[str(self.id)])