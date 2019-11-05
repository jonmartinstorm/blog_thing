from django.urls import path

from . import views
# from .views import (
#     BlogPostDetailView,
#     BlogPostListView,
#     BlogCreateFormView,
#     BlogPostUpdateView,
# )

app_name = 'blog'
urlpatterns = [
    path('', views.BlogPostListView.as_view(), name='blog-list'),
    path('show/<slug:slug>/', views.BlogPostDetailView.as_view(), name='post-detail'),
    path('edit/<slug:slug>/', views.BlogPostUpdateView.as_view(), name='post-update'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('new/', views.BlogCreateFormView.as_view(), name='post-create'),
]
