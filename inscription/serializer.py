from rest_framework import serializers


class InscriptionSerializer(serializers.Serializer):
    nom = serializers.CharField()
    email = serializers.CharField()
    mot_de_passe = serializers.CharField()