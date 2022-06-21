from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=100)


class Book(models.Model):
    book_name = models.CharField(max_length=100)


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
