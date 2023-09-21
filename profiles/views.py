from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import EntrepreneurProfile, Subscription
from .serializers import EntrepreneurProfileSerializer, SubscriptionSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


# Create your views here.


class EntrepreneurProfileList(generics.ListAPIView):
    queryset = EntrepreneurProfile.objects.all().order_by('name')
    serializer_class = EntrepreneurProfileSerializer




class SubscriptionList(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer



@api_view(['POST'])
def create_profile(request):
    # Vérifiez si l'utilisateur est authentifié
    #if not request.user.is_authenticated:
    #    return Response({'message': 'Vous devez être connecté pour créer un profil.'}, status=status.HTTP_401_UNAUTHORIZED)

    # Récupérez les données de la demande
    name = request.data.get('name')
    description = request.data.get('description')
    sector = request.data.get('sector')
    site = request.data.get('site')
    telephone = request.data.get('telephone')
    email = request.data.get('email')
    password = request.data.get('password')
    subscription_id = request.data.get('subscription_id')

    # Validez les données d'entrée (vous pouvez utiliser Django forms ou serializers)
    if not name or not description or not sector or not site:
        return Response({'message': 'Veuillez fournir toutes les informations du profil.'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        subscription = Subscription.objects.get(id=subscription_id)
    except Subscription.DoesNotExist:
        return Response({'message': 'La souscription spécifiée n\'existe pas.'}, status=status.HTTP_400_BAD_REQUEST)

    # Créez un profil utilisateur lié à l'utilisateur authentifié
    user_profile = EntrepreneurProfile(name=name, 
    description=description, sector=sector, 
    site=site, telephone=telephone,email=email, password=password,subscription=subscription)
    user_profile.save()

    return Response({'message': 'Profil créé avec succès.'}, status=status.HTTP_201_CREATED)
