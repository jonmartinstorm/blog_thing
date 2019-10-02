from django.db import models
#test
class BlogPost(models.Model):
    slug = models.SlugField(unique=True)
    title = models.TextField()
    content = models.TextField(null=True, blank=True)
