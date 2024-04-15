from django.shortcuts import render

# animas data
# animals = [
#     {"name": "Elephant", "species": "Loxodonta africana (African) or Elephas maximus (Asian)", "habitat": "Various habitats including forests, savannas, and deserts", "diet": "Herbivore"},
#     {"name": "Crocodile", "species": "Various species, such as Nile Crocodile (Crocodylus niloticus)", "habitat": "Tropical regions of Africa, Asia, the Americas, and Australia", "diet": "Carnivore (fish, birds, mammals)"},
#     {"name": "Giraffe", "species": "Giraffa camelopardalis", "habitat": "Savannas, grasslands, and open woodlands", "diet": "Herbivore"},
# ]

from .models import Animal

# Create your views here

def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def animals_index(request):
   animals = Animal.objects.all()
   return render(request, 'animals/index.html', {
      'animals': animals
   })

def animals_detail(request, animal_id): 
    animal = Animal.objects.get(id=animal_id)
    return render(request, 'animals/detail.html', {'animal': animal})
