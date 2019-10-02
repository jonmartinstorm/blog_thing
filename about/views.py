from django.shortcuts import render

def about_page(request):
    context = {
        "title": "About us",
    }
    template_name = "about.html"
    return render(request, template_name, context)
