from django.shortcuts import render
from destinations.models import Destination
from spots.models import Spots

def home(request):
    featured_destinations = Destination.objects.all().order_by('-created_at')[:3] # Just taking latest 3 as featured for now
    categories = Destination.CATEGORY_CHOICES
    
    # Simple logic to get trending forts (e.g. random or specific logic)
    trending_forts = Destination.objects.filter(category='Fort')[:4]
    
    # Fetch featured spots (e.g., top rated or latest)
    featured_spots = Spots.objects.all().order_by('-rating')[:6]

    context = {
        'featured_destinations': featured_destinations,
        'categories': [c[0] for c in categories], # Just passing the values
        'trending_forts': trending_forts,
        'featured_spots': featured_spots,
    }
    return render(request, 'core/index.html', context)
