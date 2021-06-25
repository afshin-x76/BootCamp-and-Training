from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Library(models.Model):
    name = models.CharField(max_length=255)
    book = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'libraries'