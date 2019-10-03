from django.db import models


class BlogPost(models.Model):
    slug = models.SlugField(max_length=150, unique=True)
    title = models.TextField(max_length=100)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
