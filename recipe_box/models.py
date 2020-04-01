from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField("self", symmetrical=False, default=None)
    # back populate with something

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # Deletes Recipes data that has been orphaned by deletion of Author class
    description = models.TextField()
    time_required = models.CharField(max_length=30)
    instructions = models.TextField()

    def __str__(self):
        return f"\"{self.title}\" by [{self.author}]"
