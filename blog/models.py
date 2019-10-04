from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator

User = settings.AUTH_USER_MODEL

class BlogPost(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = unique_slug_generator(self, self.title)
        super(BlogPost, self).save()
