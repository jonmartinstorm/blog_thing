from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render

from .models import BlogPost



def blog_post_detail_page(request, post_id):
    obj = BlogPost.objects.get(id=post_id)
    template_name = 'blog_post_detail.html'
    context = {
        "object": obj
    }
    return render(request, template_name, context)

def index(request):
    context = {
        "title": "Home!",
        "my_list": [1, 2, 3, 4, 5],
    }
    return render(request, "home.html", context)

def about_page(request):
    context = {
        "title": "About us",
    }
    return render(request, "hello_world.html", context)

def contact_page(request):
    context = {
        "title": "Contact us",
    }
    return render(request, "hello_world.html", context)
