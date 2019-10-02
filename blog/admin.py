from django.contrib import admin
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','id',)

admin.site.register(BlogPost, BlogPostAdmin)
