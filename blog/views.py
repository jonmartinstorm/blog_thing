from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        "title": "Hello there....",
    }
    return render(request, "hello_world.html", context)

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
