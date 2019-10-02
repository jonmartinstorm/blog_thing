from django.urls import path

from .views import (
    BlogPostDetailView,
    BlogPostListView,
    blog_post_create_view,

)

app_name = 'blog'
urlpatterns = [
    path('', BlogPostListView.as_view(), name='blog-list'),
    path('show/<slug:slug>/', BlogPostDetailView.as_view(), name='post-detail'),
    # path('post/<slug:slug>/edit/', BlogPostDetailView.as_view(), name='post-edit'),
    path('new/', blog_post_create_view, name='post-create'),
]
