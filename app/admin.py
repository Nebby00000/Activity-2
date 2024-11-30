from django.contrib import admin
from .models import UserProfile, Recipe, Ingredient, Category, Comment, Address

admin.site.register(UserProfile)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Address)

