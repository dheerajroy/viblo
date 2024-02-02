from django.db import models
from django.utils.text import slugify
from accounts.models import CustomUser
from ckeditor.fields import RichTextField


class Page(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    private = models.BooleanField(default=False, blank=True)
    content = RichTextField()
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.author} | {self.title}'
