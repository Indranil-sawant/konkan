from django.contrib import admin
from .models import Spots, Category, Tag
# Register your models here.

@admin.register(Spots)
class SpotsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'uploaded_by', 'distance', 'rating', 'created_at')
    list_filter = ('category', 'uploaded_by')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)