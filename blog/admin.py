from django.contrib import admin
from .forms import BlogPostAdminForm
from .models import BlogPost, Image, Category


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm
    #fields = "__all__"
    list_display = ('title', 'slug', 'id', 'header_image')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategroryAdmin(admin.ModelAdmin):
    pass
