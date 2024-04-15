from django.db import models
from django.urls import reverse

# Create your models here.

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)


class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)
    diet = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.id})'


    def get_absolute_url(self):
        return reverse('detail', kwargs={'animal_id': self.id})

class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
        )
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    class Meta:
        ordering = ['-date']

    