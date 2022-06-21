from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


class Author(models.Model):
    full_name = models.CharField(max_length=100)


class Book(models.Model):
    book_name = models.CharField(max_length=100)


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
