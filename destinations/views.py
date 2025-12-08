from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Destination
from .forms import DestinationForm
from reviews.models import Review
from reviews.forms import ReviewForm 

@login_required
def destination_list(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    destinations = Destination.objects.filter(is_verified=True)

    if query:
        destinations = destinations.filter(
            Q(title__icontains=query) | Q(location_name__icontains=query)
        )
    
    if category:
        destinations = destinations.filter(category=category)

    context = {
        'destinations': destinations,
        'category': category,
        'query': query
    }
    return render(request, 'destinations/destination_list.html', context)

@login_required
def temples(request):
    destinations = Destination.objects.filter(category='Temple', is_verified=True)
    context = {
        'destinations': destinations,
        'category': 'Temple',
    }
    return render(request, 'destinations/destination_list.html', context)

@login_required
def create_destination(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            destination = form.save(commit=False)
            destination.submitted_by = request.user
            destination.is_verified = False # Explicitly set to False
            destination.save()
            return render(request, 'destinations/submission_success.html') # Redirect to a success page or render a success message
    else:
        form = DestinationForm()
    
    return render(request, 'destinations/destination_form.html', {'form': form})

@login_required
def destination_detail(request, slug):
    destination = get_object_or_404(Destination, slug=slug)
    # Optional: Check if verified or owner
    # if not destination.is_verified and destination.submitted_by != request.user:
    #    raise Http404 
    
    reviews = destination.reviews.all().order_by('-created_at')
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.destination = destination
            if request.user.is_authenticated:
                review.user = request.user
            review.save()
            return redirect('destination_detail', slug=slug)
    else:
        form = ReviewForm()

    context = {
        'destination': destination,
        'reviews': reviews,
        'review_form': form,
    }
    return render(request, 'destinations/destination_detail.html', context)
