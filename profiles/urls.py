from django.urls import path
from . import views
from .views import EntrepreneurProfileList

urlpatterns = [
    path('profiles/', EntrepreneurProfileList.as_view(), name='profiles'),
    path('subscriptions/', views.SubscriptionList.as_view(), name='subscription-list'),
    path('create-profile/', views.create_profile),
]