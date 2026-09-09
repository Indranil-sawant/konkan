from django.shortcuts import render
from destinations.models import Destination
from spots.models import Spots
from food.models import FoodItem

def home(request):
    featured_destinations = Destination.objects.filter(is_verified=True).order_by('-created_at')[:8]
    categories = Destination.CATEGORY_CHOICES
    
    trending_forts = Destination.objects.filter(category='Fort', is_verified=True)[:4]
    
    featured_spots = Spots.objects.all().order_by('-rating')[:6]

    context = {
        'featured_destinations': featured_destinations,
        'categories': [c[0] for c in categories],
        'trending_forts': trending_forts,
        'featured_spots': featured_spots,
        'featured_food': FoodItem.objects.all().order_by('-rating')[:6],
    }
    return render(request, 'core/index.html', context)


def search(request):        
    query = request.GET.get('q', '').strip()
    if query:
        destination_results = Destination.objects.filter(title__icontains=query, is_verified=True)
        spot_results = Spots.objects.filter(name__icontains=query)
        food_results = FoodItem.objects.filter(name__icontains=query)
    else:
        destination_results = Destination.objects.none()
        spot_results = Spots.objects.none()
        food_results = FoodItem.objects.none()

    context = {
        'query': query,
        'destination_results': destination_results,
        'spot_results': spot_results,
        'food_results': food_results,
    }
    return render(request, 'core/search_results.html', context)
                 