from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import EntrepreneurProfile
from .serializers import EntrepreneurProfileSerializer


# Create your views here.


class EntrepreneurProfileList(generics.ListAPIView):
    queryset = EntrepreneurProfile.objects.all().order_by('name')
    serializer_class = EntrepreneurProfileSerializer


@api_view(['POST'])
def create_profile(request):
    if request.method == 'POST':
        serializer = EntrepreneurProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)