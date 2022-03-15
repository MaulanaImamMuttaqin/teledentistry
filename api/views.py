from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# Create your views here.
class TestView(APIView):
    permission_classes  = [IsAuthenticated]
    def post(self, request):
        return Response(request.data, status=status.HTTP_200_OK)
