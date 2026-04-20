from django.shortcuts import render
from django.db.models import Q
from destinations.models import Destination
from spots.models import Spots
from food.models import FoodItem


def home(request):
    featured_destinations = Destination.objects.all().order_by('-created_at')[:3]
    categories = Destination.CATEGORY_CHOICES

    trending_forts = Destination.objects.filter(category='Fort')[:4]
    featured_spots = Spots.objects.all().order_by('-rating')[:6]

    context = {
        'featured_destinations': featured_destinations,
        'categories': [c[0] for c in categories],
        'trending_forts': trending_forts,
        'featured_spots': featured_spots,
        'featured_food': FoodItem.objects.all().order_by('-rating')[:6],
    }
    return render(request, 'core/index.html', context)


def destination_detail(request, id):
    destination = Destination.objects.get(id=id)
    return render(request, 'core/destination_detail.html', {'destination': destination})


def details_spots(request, id):
    spot = Spots.objects.get(id=id)
    return render(request, 'core/spot_detail.html', {'spot': spot})


def food_detail(request, id):
    food = FoodItem.objects.get(id=id)
    return render(request, 'core/food_detail.html', {'food': food})


def search(request):
    query = request.GET.get('q', '')

    destination_results = Destination.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query) |
        Q(location_name__icontains=query)
    ) if query else Destination.objects.none()

    spot_results = Spots.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query)
    ) if query else Spots.objects.none()

    food_results = FoodItem.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query)
    ) if query else FoodItem.objects.none()

    context = {
        'query': query,
        'destination_results': destination_results,
        'spot_results': spot_results,
        'food_results': food_results,
    }
    return render(request, 'core/search_results.html', context)