from rest_framework import serializers
from .models import Hotel


class HotelSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ['id', 'nom', 'ville', 'prix', 'adresse', 'image', 'created_at']

    def get_image(self, obj):
        """Retourne l'URL complète de l'image Cloudinary"""
        if obj.image:
            try:
                # Cloudinary retourne déjà une URL complète
                return obj.image.url
            except:
                return None
        return None