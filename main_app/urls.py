from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    #route for animals index
    path('animals/', views.animals_index, name='index'),
    path('animals/<int:animal_id>/', views.animals_detail, name='detail'),
    path('animals/create/', views.AnimalCreate.as_view(), name = 'animals_create'),
    path('animals/<int:pk>/update/', views.AnimalUpdate.as_view(), name='animals_update'),
    path('animals/<int:pk>/delete/', views.AnimalDelete.as_view(), name='animals_delete'), 
    path('animals/<int:animal_id>/add_feeding/', views.add_feeding, name='add_feeding'), 
    path('foods/', views.FoodList.as_view(), name='foods_index'),
    path('foods/<int:pk>/', views.FoodDetail.as_view(), name='foods_detail'),
    path('foods/create/', views.FoodCreate.as_view(), name='foods_create'),
    path('foods/<int:pk>/update/', views.FoodUpdate.as_view(), name='foods_update'),
    path('foods/<int:pk>/delete/', views.FoodDelete.as_view(), name='foods_delete'),
    path('animals/<int:animal_id>/assoc_food/<int:food_id>/', views.assoc_food, name='assoc_food'),
    path('foods/<int:animal_id>/remove_food/<int:food_id>/', views.remove_food, name='remove_food'),

]