from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient

class RecipeInLine(admin.TabularInline):
    model = Recipe

class IngredientInLine(admin.TabularInline): 
    model = Ingredient 

class RecipeIngredientInLine(admin.TabularInline): 
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin): 
    model = Recipe
    inlines = [RecipeIngredientInLine,]
    
    list_display = ['name']

admin.site.register(Recipe, RecipeAdmin)