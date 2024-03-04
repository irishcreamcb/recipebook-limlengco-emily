from django.db import models
from django.urls import reverse

class Ingredient(models.Model): 
    name = models.CharField(max_length=100)

    def __str__(self): 
        return self.name
    
    def get_absolute_url(self): 
        return reverse('ingredient_detail', args=[str(self.name)])

class Recipe(models.Model): 
    name = models.CharField(max_length=100)

    def __str__(self): 
        return self.name
    
    def get_absolute_url(self): 
        return reverse('ledger:recipe-detail', args=[str(self.name)])

class RecipeIngredient(models.Model): 
    quantity = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, 
                               on_delete=models.CASCADE, 
                               related_name='ingredients')
    ingredient = models.ForeignKey(Ingredient, 
                                   on_delete=models.CASCADE,
                                   related_name='recipe')

    def __str__(self): 
        return '{} of {}'.format(self.quantity, self.ingredient)