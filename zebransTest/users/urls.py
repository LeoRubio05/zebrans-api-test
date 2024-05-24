from django.urls import path
from .views import MyTokenObtainPairView, RegisterView, ProfileView, UpdateView, DeleteView

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('profile/', ProfileView.as_view(), name='user_profile'),
    path('update/', UpdateView.as_view(), name='update_profile'),
    path('delete/<int:pk>/', DeleteView.as_view(), name='delete_profile'),
]
