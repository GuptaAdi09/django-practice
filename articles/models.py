from django.db import models

# Create your models here.
# creating a simple model for article 
class Articles(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100,default="Unknown")
    discription = models.TextField(max_length=1000)

class Writer(models.Model):
    name = models.ForeignKey(Articles,on_delete=models.CASCADE)
    age = models.IntegerField()
    born_in = models.CharField(max_length=100, default=None)
    experience = models.IntegerField()
    is_alive = models.BooleanField(default=False)