from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .models import Products
from .serializers import ProductsSerializer


class ProductsList(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


@permission_classes([IsAuthenticated])
class ProductCreate(generics.CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


@permission_classes([IsAuthenticated])
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
