from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Type(models.Model):
    type = models.CharField(max_length=240, verbose_name='Шакл')

    def __str__(self):
        return self.type


class Category(models.Model):
    category = models.CharField(max_length=200, verbose_name='Бахш')

    def __str__(self):
        return self.category


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True)
    annotation = RichTextField(blank=True, null=True)
    text = RichTextField(blank=True, null=True)
    source = RichTextField(blank=True, null=True)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    pubdate = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    views = models.IntegerField(default=0)

    class Meta:
        ordering = ['-pubdate']

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField("Ном:", max_length=255)
    email = models.EmailField()
    body = models.TextField("")
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'


