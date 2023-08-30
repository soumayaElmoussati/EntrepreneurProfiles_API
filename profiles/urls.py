from django.urls import path
from . import views
from .views import EntrepreneurProfileList

urlpatterns = [
    path('profiles/', EntrepreneurProfileList.as_view(), name='profile-list'),
    path('create/', views.create_profile, name='create-profile'),
]