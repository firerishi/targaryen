from django.db import models

# Create your models here.

class Post(models.Model):
    content = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')
