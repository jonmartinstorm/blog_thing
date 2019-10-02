from django.shortcuts import render

def contact_page(request):
    context = {
        "title": "Contact us",
    }
    template_name = "contact.html"
    return render(request, template_name, context)
