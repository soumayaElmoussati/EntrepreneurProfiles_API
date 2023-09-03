from rest_framework import serializers
from .models import EntrepreneurProfile, Subscription

class EntrepreneurProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntrepreneurProfile
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'