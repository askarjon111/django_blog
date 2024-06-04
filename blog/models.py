from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=500, verbose_name="Sarlavha")
    body = models.TextField(blank=True, null=True)
    cover = models.ImageField(upload_to="posts/images", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title