from django.db import models
from django.urls import reverse

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)
    diet = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.id})'


    def get_absolute_url(self):
        return reverse('detail', kwargs={'animal_id': self.id})