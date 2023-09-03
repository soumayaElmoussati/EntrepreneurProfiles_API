from django.urls import path
from . import views
from .views import EntrepreneurProfileList

urlpatterns = [
    path('profiles/', EntrepreneurProfileList.as_view(), name='profiles'),
    #path('create/', views.create_profile, name='create'),
    path('profiles/<int:profile_id>/', views.delete_profile, name='delete_profile'),
    path('subscriptions/', views.SubscriptionList.as_view(), name='subscription-list'),
    path('register/', views.register),
    path('create-profile/', views.create_profile),
]