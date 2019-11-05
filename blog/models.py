from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
from .utils import unique_slug_generator

User = settings.AUTH_USER_MODEL

class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)

class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="image/", blank=False, null=True)

    def __str__(self):
        return self.image.url

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    header_image = models.ForeignKey(Image, blank=False, null=True, on_delete=models.SET_NULL, related_name="header_image")
    content_images = models.ManyToManyField(Image, related_name="content_images", blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = BlogPostManager()

    class Meta:
        # ordering = ['-publish_date', '-updated', '-timestamp']
        ordering = ['-publish_date']
        base_manager_name = 'objects'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = unique_slug_generator(self, self.title)
        super(BlogPost, self).save()
