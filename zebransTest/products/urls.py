from django.urls import path
from .views import ProductsList, ProductDetail

# This is the list of our routes
urlpatterns = [
    path('', ProductsList.as_view()),
    path('<str:pk>/', ProductDetail.as_view())
]
