from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import Profileform
from spots.models import Spots
from reviews.models import Review


def _get_profile_context(profile):
    spots_qs = Spots.objects.filter(uploaded_by=profile).select_related('category').order_by('-created_at')
    reviews_qs = (
        Review.objects.filter(user=profile.user).select_related('destination').order_by('-created_at')
        if profile.user else Review.objects.none()
    )
    return {
        'profile':      profile,
        'spots':        spots_qs[:6],
        'reviews':      reviews_qs[:6],
        'spot_count':   spots_qs.count(),
        'review_count': reviews_qs.count(),
    }


@login_required
def users(request):
    profiles = Profile.objects.all()
    return render(request, 'users/users.html', {'profiles': profiles})


@login_required
def create_users(request):
    users_form = Profileform()
    if request.method == 'POST':
        users_form = Profileform(request.POST, request.FILES)
        if users_form.is_valid():
            users_form.save()
            return redirect('home')
    return render(request, 'users/users_form.html', {'users_form': users_form})


@login_required
def user_page(request, pk):
    profile = Profile.objects.get(id=pk)
    return render(request, 'users/user_profile.html', _get_profile_context(profile))


@login_required
def my_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(
            user=request.user,
            username=request.user.username,
            name=request.user.first_name,
            email=request.user.email,
        )
    return render(request, 'users/user_profile.html', _get_profile_context(profile))