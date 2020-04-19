from django.db import models

# Create your models here.

class Article(models.Model):

    Author = models.CharField(max_length=200)
    Title = models.CharField(max_length=200)
    Email = models.EmailField(max_length=100)
    Date = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.Title

