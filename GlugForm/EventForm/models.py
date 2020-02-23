from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    dept= models.CharField(max_length=30)
    usn = models.CharField(max_length=30)
    email = models.EmailField()
    