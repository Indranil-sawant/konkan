from django.contrib import admin
from .models import Spots, Category, Tag
# Register your models here.

@admin.register(Spots)
class SpotsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'uploaded_by', 'distance', 'rating', 'created_at')
    list_filter = ('category', 'uploaded_by', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Spot Details', {
            'fields': ('name', 'category', 'tags', 'rating', 'description')
        }),
        ('Location & Media', {
            'fields': ('distance', 'map_link', 'photo')
        }),
        ('Additional Info', {
            'fields': ('ingredients',),
            'classes': ('collapse',),
        }),
        ('Attribution', {
            'fields': ('uploaded_by',),
            'classes': ('collapse',),
        }),
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)