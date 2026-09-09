from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Operations Control Center & Tourism CMS
    path('ops/', include('ops.urls')),

    # Standard Django Admin
    path('admin/', admin.site.urls),

    # HTML views
    path('', include('core.urls')),
    path('', include('companion.urls')),
    path('spots/', include('spots.urls')),
    path('destinations/', include('destinations.urls')),
    path('accounts/', include('accounts.urls')),
    path('food/', include('food.urls')),
    path('users/', include('users.urls')),

    # REST API
    path('api/v1/', include('api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
