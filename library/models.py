from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=123)
    subtitle = models.CharField(max_length=123)
    author = models.CharField(max_length=123)
    isbn = models.CharField(max_length=123)
    price = models.DecimalField(max_digits=123, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
