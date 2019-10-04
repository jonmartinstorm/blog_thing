from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import BlogPostModelForm
from .models import BlogPost

class BlogPostListView(ListView):
    model = BlogPost
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class BlogCreateFormView(LoginRequiredMixin, FormView):
    template_name = "blog/create.html"
    form_class = BlogPostModelForm
    success_url = '.'
    login_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)

class BlogPostDetailView(DetailView):
    model = BlogPost

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
