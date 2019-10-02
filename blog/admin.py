from django.contrib import admin
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'id',)

admin.site.register(BlogPost, BlogPostAdmin)
