from django.urls import path

from .views import (
    BlogPostDetailView,
    BlogPostListView,
    about_page,
    contact_page,
    blog_post_create_view,

)

app_name = 'blog'
urlpatterns = [
    path('', BlogPostListView.as_view(), name='blog-list'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('post/<slug:slug>/', BlogPostDetailView.as_view(), name='post-detail'),
    # path('post/<slug:slug>/edit/', BlogPostDetailView.as_view(), name='post-edit'),
    path('post-new/', blog_post_create_view, name='post-create'),
]
