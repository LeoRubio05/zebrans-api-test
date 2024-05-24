from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (MyTokenObtainPairSerializer,
                          RegisterSerializer,
                          ProfileSerializer,
                          UpdateSerializer)
from .models import CustomUser


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser,)
    serializer_class = RegisterSerializer


class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)


class UpdateView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser,)
    queryset = CustomUser.objects.all()
    serializer_class = UpdateSerializer

    def get_object(self):
        return self.request.user


class DeleteView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser,)
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer
