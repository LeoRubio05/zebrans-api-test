from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import permission_classes
from .models import Products
from .serializers import ProductsSerializer
from django.core.mail import send_mail
from zebransTest.settings import EMAIL_HOST_USER


class ProductsList(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


@permission_classes([IsAdminUser])
class ProductCreate(generics.CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


@permission_classes([IsAdminUser])
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    # def perform_update(self, serializer):
    #     instance = serializer.save()
    #     send_mail(
    #         "Producto modificado",
    #         "Producto modificado",
    #         EMAIL_HOST_USER,
    #         ["lefaru@gmail.com"],
    #         fail_silently=False,
    #     )
