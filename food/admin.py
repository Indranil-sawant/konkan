from django.contrib import admin

# Register your models here.
from .models import FoodItem, Tag   , Category

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'rating', 'created_at')
    list_filter = ('category', 'tags')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)