from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('destination/<int:id>/', views.destination_detail, name='destination_detail'),
    path('spot/<uuid:id>/', views.details_spots, name='details_spots'),
    path('food/<uuid:id>/', views.food_detail, name='food_detail'),
    path('search/', views.search, name='search'),
]
