from django.shortcuts import render
from .forms import ContactForm

def contact_page(request):
    template_name = "form.html"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()

    context = {
        "title": "Contact us",
        "form": form,
    }

    return render(request, template_name, context)
