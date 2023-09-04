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


#@api_view(['POST'])
#def create_profile(request):
  #  if request.method == 'POST':
  #      serializer = EntrepreneurProfileSerializer(data=request.data)
  #      if serializer.is_valid():
   #         serializer.save()
   #         return Response(serializer.data, status=status.HTTP_201_CREATED)
   #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_profile(request, profile_id):
    try:
        profile = EntrepreneurProfile.objects.get(pk=profile_id)
    except EntrepreneurProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubscriptionList(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


@api_view(['POST'])
def register(request):
    # Récupérez les données de la demande
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    # Validez les données d'entrée (vous pouvez utiliser Django forms ou serializers)
    if not username or not password or not email:
        return Response({'message': 'Veuillez fournir un nom d\'utilisateur, un mot de passe et un e-mail.'}, status=status.HTTP_400_BAD_REQUEST)

    # Créez un nouvel utilisateur
    user = User.objects.create_user(username=username, password=password, email=email)
    user.save()

    # Créez un jeton d'authentification pour l'utilisateur
    token, created = Token.objects.get_or_create(user=user)

    return Response({'message': 'Inscription réussie', 'token': token.key}, status=status.HTTP_201_CREATED)



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

    # Validez les données d'entrée (vous pouvez utiliser Django forms ou serializers)
    if not name or not description or not sector or not site:
        return Response({'message': 'Veuillez fournir toutes les informations du profil.'}, status=status.HTTP_400_BAD_REQUEST)

    # Créez un profil utilisateur lié à l'utilisateur authentifié
    user_profile = EntrepreneurProfile(user=request.user, name=name, description=description, sector=sector, site=site)
    user_profile.save()

    return Response({'message': 'Profil créé avec succès.'}, status=status.HTTP_201_CREATED)
