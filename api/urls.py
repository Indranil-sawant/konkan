"""
Central API router for Konkan Guide REST API (v1).

All API endpoints are prefixed with /api/v1/ from config/urls.py.
"""
from django.urls import path

from spots.api_views import SpotListCreateView, SpotDetailView
from food.api_views import FoodItemListCreateView, FoodItemDetailView

urlpatterns = [
    # ── Spots ──────────────────────────────────────────────────────────────
    # GET  /api/v1/spots/           → list all spots (paginated)
    # POST /api/v1/spots/           → create a spot (auth required)
    path('spots/', SpotListCreateView.as_view(), name='api-spots-list'),

    # GET    /api/v1/spots/<uuid>/  → get single spot
    # PUT    /api/v1/spots/<uuid>/  → full update (owner only)
    # PATCH  /api/v1/spots/<uuid>/  → partial update (owner only)
    # DELETE /api/v1/spots/<uuid>/  → delete (owner only)
    path('spots/<uuid:pk>/', SpotDetailView.as_view(), name='api-spots-detail'),

    # ── Food ───────────────────────────────────────────────────────────────
    path('food/', FoodItemListCreateView.as_view(), name='api-food-list'),
    path('food/<uuid:pk>/', FoodItemDetailView.as_view(), name='api-food-detail'),
]
