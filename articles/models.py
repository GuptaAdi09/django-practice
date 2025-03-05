from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import pre_save



# Create your models here.
# creating a simple model for article 
class Articles(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True,null=True)
    author = models.CharField(max_length=100,default="Unknown")
    discription = models.TextField(max_length=1000)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    

