from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView

from .forms import BlogPostForm
from .models import BlogPost

class BlogPostListView(ListView):
    model = BlogPost
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

def blog_post_create_view(request):
    template_name = "blog/create_test.html"
    form = BlogPostForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = BlogPostForm()
    context = {
        "title": "Create new post",
        "form": form,
    }
    return render(request, template_name, context)

class BlogCreateFormView(FormView):
    template_name = "blog/create_test.html"
    form_class = BlogPostForm
    success_url = '.'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)

class BlogPostDetailView(DetailView):
    model = BlogPost
    # template_name = "blog_post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        # print("Django:", self.request.method, self.request.path, self.request.user)
        return context

def blog_post_update_view(request):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/update.html'
    context = {
        "object": obj
    }
    return render(request, template_name, context)

def blog_post_delete_view(request):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    context = {
        "object": obj
    }
    return render(request, template_name, context)
