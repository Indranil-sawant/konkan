from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Destination(models.Model):
    CATEGORY_CHOICES = (
        ('Fort', 'Fort'),
        ('Beach', 'Beach'),
        ('Waterfall', 'Waterfall'),
        ('Temple', 'Temple'),
        ('Viewpoint', 'Viewpoint'),
        ('Food', 'Food Spot'),
        ('Other', 'Other'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    location_name = models.CharField(max_length=200)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    main_image = models.ImageField(upload_to='destinations/main/')
    best_time_to_visit = models.CharField(max_length=200, blank=True)
    travel_tips = models.TextField(blank=True)
    entry_fees = models.CharField(max_length=200, blank=True, default='Free')
    timings = models.CharField(max_length=200, blank=True)
    is_verified = models.BooleanField(default=False)
    submitted_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Ensure slug is unique if possible, simply slugifying title might duplicate
            # For now, let's keep it simple as per original, but append something if needed could be better
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('destination_detail', kwargs={'slug': self.slug})

class Gallery(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='destinations/gallery/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Image for {self.destination.title}"
