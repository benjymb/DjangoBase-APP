from . import models
from .functions import longest_word
from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):

    queryset = models.Product.objects.all().order_by('-created')
    serializer_class = ProductSerializer

class ShearchCoords(views.APIView):
    
    def get(self, request, format=None):
        names = models.Product.get_names()
        longest = longest_word(
            request.query_params.get('product'),
            names.keys()
        )
        if longest:
            product = models.Product.objects.get(reference=names[longest])
            return Response(ProductSerializer(product).data)
        else:
            return Response(None)
