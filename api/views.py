from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import generics
from django.contrib.auth import get_user_model

from auth_api.serializers import UserSerializer

# Create your views here.
class TestView(APIView):
    permission_classes  = [IsAuthenticated]
    def post(self, request):
        return Response(request.data, status=status.HTTP_200_OK)



class UserProfile(generics.RetrieveUpdateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes  = [IsAuthenticated]
    serializer_class = UserSerializer



