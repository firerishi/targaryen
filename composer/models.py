from django.db import models

# Create your models here.

class Post(models.Model):
    content = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')


class Page(models.Model):
    content = models.CharField(max_length=2000)
    url = models.CharField(max_length=256)
    pub_date = models.DateTimeField('date published')
