from . import models
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):

    queryset = models.Product.objects.all().order_by('-created')
    serializer_class = ProductSerializer
