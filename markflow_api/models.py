from django.db import models


class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Document(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
