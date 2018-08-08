from django.contrib import admin

from .models import Blog

@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_date', 'published_date', 'edited_date')
	search_fields = ('title', 'content')