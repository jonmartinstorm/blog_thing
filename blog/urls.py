from django.urls import path

from .views import (
    BlogPostDetailView,
    BlogPostListView,
    BlogCreateFormView,
    BlogPostUpdateView,
)

app_name = 'blog'
urlpatterns = [
    path('', BlogPostListView.as_view(), name='blog-list'),
    path('show/<slug:slug>/', BlogPostDetailView.as_view(), name='post-detail'),
    path('edit/<slug:slug>/', BlogPostUpdateView.as_view(), name='post-update'),
    path('new/', BlogCreateFormView.as_view(), name='post-create'),
]
