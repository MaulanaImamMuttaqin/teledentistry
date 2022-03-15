from django.urls import path
from .views import TestView

urlpatterns = [
    path('get_data/', TestView.as_view(), name='test get data'),
]