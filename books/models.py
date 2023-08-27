from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    publisher = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.title