from django.urls import path
from .views import TestView, UserProfile

urlpatterns = [
    path('get_data/', TestView.as_view(), name='test get data'),
    path('user_profile/<int:pk>', UserProfile.as_view())
]