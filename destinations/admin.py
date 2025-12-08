from django.contrib import admin
from .models import Destination, Gallery

class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 1

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location_name', 'is_verified', 'created_at')
    list_filter = ('is_verified', 'category')
    list_editable = ('is_verified',)
    search_fields = ('title', 'location_name')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [GalleryInline]

admin.site.register(Gallery)
