from django.urls import include, path
from rest_framework import routers
from valerdat import views

valerdat_router = routers.DefaultRouter()
valerdat_router.register(r'products', views.ProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.




from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('valerdat/', include(valerdat_router.urls)),
    path('valerdat/shearchcoords/', views.ShearchCoords.as_view(), name="shearcoords"),
]
