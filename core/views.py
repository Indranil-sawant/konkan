from django.shortcuts import render
from destinations.models import Destination
from spots.models import Spots
from food.models import FoodItem
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
        'featured_food': FoodItem.objects.all().order_by('-rating')[:6], # Top rated food items
    }
    return render(request, 'core/index.html', context)


def destination_detail(request, id):
    destination = Destination.objects.get(id=id)
    context = {
        'destination': destination,
    }
    return render(request, 'core/destination_detail.html', context)     

def details_spots(request, id):     
    spot = Spots.objects.get(id=id)
    context = {
        'spot': spot,
    }
    return render(request, 'core/spot_detail.html', context)                        

def food_detail(request, id):           
    food = FoodItem.objects.get(id=id)
    context = {
        'food': food,
    }
    return render(request, 'core/food_detail.html', context)        

def search(request):        
    query = request.GET.get('q', '')
    destination_results = Destination.objects.filter(name__icontains=query)
    spot_results = Spots.objects.filter(name__icontains=query)
    food_results = FoodItem.objects.filter(name__icontains=query)

    context = {
        'query': query,
        'destination_results': destination_results,
        'spot_results': spot_results,
        'food_results': food_results,
    }
    return render(request, 'core/search_results.html', context)                 