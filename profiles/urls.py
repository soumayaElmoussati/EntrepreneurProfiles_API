from django.urls import path
from . import views
from .views import EntrepreneurProfileList

urlpatterns = [
    path('profiles/', EntrepreneurProfileList.as_view(), name='profile-list'),
    path('api/profiles/', views.create_profile, name='create-profile'),
]