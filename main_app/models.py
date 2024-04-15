from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)
    diet = models.CharField(max_length=100)

def __str__(self):
    return self.name