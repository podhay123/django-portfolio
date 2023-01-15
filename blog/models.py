from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=10)
    date = models.DateField()
    category = models.CharField(max_length=25)
    description = models.TextField()


class Coment(models.Model):
    username = models.CharField(max_length=15)
    content = models.CharField(max_length=100)
    postnumer = models.IntegerField()
