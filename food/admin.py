from django.contrib import admin

# Register your models here.
from .models import FoodItem, Tag   , Category

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'rating', 'created_at')
    list_filter = ('category', 'tags', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Dish Details', {
            'fields': ('name', 'category', 'tags', 'price', 'rating', 'photo')
        }),
        ('Narrative & Recipe', {
            'fields': ('description', 'ingredients', 'recipe_link', 'best_time_to_eat')
        }),
        ('Health Info', {
            'fields': ('calories',),
            'classes': ('collapse',),
        }),
        ('Ownership', {
            'fields': ('uploaded_by',),
            'classes': ('collapse',),
        }),
    )

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)