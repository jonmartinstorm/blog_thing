from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import BlogPost

# def index(request):
#     context = {
#         "title": "Home!",
#         "my_list": [1, 2, 3, 4, 5],
#     }
#     return render(request, "home.html", context)

def blog_post_list_view(request):
    qs = BlogPost.objects.all()
    template_name = "blog_post_list.html"
    context = {
        'object_list': qs
    }
    return render(request, template_name, context)

class BlogPostListView(ListView):
    model = BlogPost
    paginate_by = 20
    # template_name = "blog_post_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

def blog_post_create_view(request):
    template_name = "blog_post_create.html"
    context = {
        'form': None,
    }
    return render(request, template_name, context)

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
    template_name = 'blog_post_update.html'
    context = {
        "object": obj
    }
    return render(request, template_name, context)

def blog_post_delete_view(request):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_delete.html'
    context = {
        "object": obj
    }
    return render(request, template_name, context)
