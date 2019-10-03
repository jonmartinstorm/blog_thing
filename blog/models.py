from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator


class BlogPost(models.Model):
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    title = models.TextField(max_length=100)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self):
        self.slug = unique_slug_generator(self, self.title)
        super(BlogPost, self).save()
