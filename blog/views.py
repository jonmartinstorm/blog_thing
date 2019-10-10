from django.utils import timezone
# from django.http import HttpResponse
# from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import BlogPostModelForm
from .models import BlogPost

class BlogPostListView(ListView):
    model = BlogPost
    paginate_by = 20

    def get_queryset(self):
        return BlogPost.objects.all().published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context

class BlogCreateFormView(LoginRequiredMixin, FormView):
    template_name = "blog/create.html"
    form_class = BlogPostModelForm
    object = None

    # 403 if user is not logged in.
    raise_exception = True

    def get_success_url(self):
        return self.object.get_absolute_url()

    def form_valid(self, form):
        form.instance.author = self.request.user
        self.object = form.save()
        return super().form_valid(form)

class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class BlogPostUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    template_name = "blog/update.html"
    form_class = BlogPostModelForm

    # 403 if user is not logged in.
    raise_exception = True

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)
