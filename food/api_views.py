from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import FoodItem
from .serializers import FoodItemSerializer
from config.permissions import IsOwnerOrReadOnly


class FoodItemListCreateView(generics.ListCreateAPIView):
    """
    GET  /api/v1/food/   → List all food items (paginated, searchable)
    POST /api/v1/food/   → Create a new food item (must be logged in)

    Query parameters:
        ?search=seafood    → search name & description
        ?ordering=-rating  → sort by rating descending
        ?page=2            → page number
    """
    queryset = (
        FoodItem.objects
        .select_related('uploaded_by')
        .order_by('-rating')
    )
    serializer_class = FoodItemSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['rating', 'price', 'created_at']
    ordering = ['-rating']

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user.profile)


class FoodItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/v1/food/<uuid>/  → Retrieve a single food item
    PUT    /api/v1/food/<uuid>/  → Full update (owner only)
    PATCH  /api/v1/food/<uuid>/  → Partial update (owner only)
    DELETE /api/v1/food/<uuid>/  → Delete (owner only)
    """
    queryset = FoodItem.objects.select_related('uploaded_by').all()
    serializer_class = FoodItemSerializer
    permission_classes = [IsOwnerOrReadOnly]
