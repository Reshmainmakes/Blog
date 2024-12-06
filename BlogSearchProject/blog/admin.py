from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at')  # Fields to display in the admin list view
    search_fields = ('title', 'content', 'author')  # Fields to search in the admin
    list_filter = ('category', 'created_at')  # Fields to filter by in the admin sidebar
    ordering = ('-created_at',)  # Order by creation date descending
