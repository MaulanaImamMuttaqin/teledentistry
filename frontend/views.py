from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
# Create your views here.


class HomeView(APIView):
    renderer_class = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        return Response()
