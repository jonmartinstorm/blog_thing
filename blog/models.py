from django.db import models

class BlogPost(models.Model):
    slug = models.SlugField(unique=True)
    title = models.TextField()
    content = models.TextField(null=True, blank=True)
