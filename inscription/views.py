from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from .models import users
from .serializer import InscriptionSerializer


class InscriptionViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'], url_path='register')
    def register(self, request):
        serializer = InscriptionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        users.objects.create(
            nom=serializer.validated_data['nom'],
            email=serializer.validated_data['email'],
            mot_de_passe=serializer.validated_data['mot_de_passe']
        )

        return Response({"message": "Compte créé"}, status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    email = request.data.get('email', '').strip()
    mot_de_passe = request.data.get('mot_de_passe', '').strip()

    user = users.objects.filter(email__iexact=email, mot_de_passe=mot_de_passe).first()

    if user:
        return Response({
            "message": "Connexion réussie",
            "user": {
                "id": user.id,
                "nom": user.nom,
                "email": user.email
            }
        }, status=status.HTTP_200_OK)
    else:
        return Response(
            {"message": "Email ou mot de passe incorrect"},
            status=status.HTTP_401_UNAUTHORIZED
        )
