from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=50, help_text="Title for our blog", unique_for_date="published_date")
	content = models.TextField(help_text="Content for our blog")
	created_date = models.DateTimeField(auto_now_add=True, help_text="Date on which the blog is made")
	published_date = models.DateField(help_text="Date on which the blog will be published", verbose_name="Published Date")
	edited_date = models.DateField(auto_now=True)