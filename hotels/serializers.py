from rest_framework import serializers
from .models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    class Meta:
        model = Hotel
        fields = ['id', 'nom', 'ville', 'prix', 'adresse', 'image', 'created_at']
