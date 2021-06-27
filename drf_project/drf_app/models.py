from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick_name = models.CharField(max_length=255)

    def __str__(self):
        return self.nick_name


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent_cat = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name_plural = 'Categories'


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
