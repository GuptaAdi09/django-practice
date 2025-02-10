from django.db import models

# Create your models here.
# creating a simple model for article 
class Articles(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100,default="Unknown")
    discription = models.TextField(max_length=1000)
