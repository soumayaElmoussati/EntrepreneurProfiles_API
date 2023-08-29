from rest_framework import serializers
from .models import EntrepreneurProfile

class EntrepreneurProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntrepreneurProfile
        fields = '__all__'

