
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Spots
from .forms import SpotsForm

# Create your views here.

def spots_home(request):
    spots = Spots.objects.all()
    context = { 'spots': spots }
    return render(request, 'spots/index.html', context)

@login_required
def create_spot(request):
    spots_form = SpotsForm()
    if request.method == 'POST':
        spots_form = SpotsForm(request.POST, request.FILES)
        if spots_form.is_valid():
            spot = spots_form.save(commit=False)
            spot.uploaded_by = request.user.profile
            spot.save()
            return redirect('home_spots')
    return render(request, 'spots/spot_form.html', {'spots_form': spots_form})


@login_required
def update_spot(request, pk):
    spots = get_object_or_404(Spots, id=pk)
    spots_form = SpotsForm(instance=spots)
    if request.method == 'POST':
        spots_form = SpotsForm(request.POST, request.FILES, instance=spots)
        if spots_form.is_valid():
            spots_form.save()
            return redirect('home_spots')
    return render(request, 'spots/spot_form.html', {'spots_form': spots_form})


@login_required
def delete_spot(request, pk):
    spots = get_object_or_404(Spots, id=pk)
    if request.method == 'POST':
        spots.delete()
        return redirect('home_spots')
    return render(request, 'spots/delete.html', {'spots': spots})


def home3(request, pk):
    spots = get_object_or_404(Spots, id=pk)
    context = {'spots': spots}
    return render(request, 'spots/details.html', context)