from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer

from .serializers import ProductSerializer
from .models import Product

class ProductResource(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer