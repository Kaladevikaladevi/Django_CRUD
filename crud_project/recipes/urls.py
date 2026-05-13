from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),

    path('delete-recipe/<id>/',
         views.delete_recipe,
         name='delete_recipe'),

    path('update-recipe/<id>/',
         views.update_recipe,
         name='update_recipe'),
]