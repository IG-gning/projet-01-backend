from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from .models import users
from .serializer import InscriptionSerializer


class InscriptionViewSet(viewsets.ViewSet):

    @action(methods=['post'], detail=False, url_path='register')
    def inscription(self, request):
        serializer = InscriptionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_dict = serializer.validated_data
        user = users(
            nom=user_dict['nom'],
            email=user_dict['email'],
            mot_de_passe=user_dict['mot_de_passe']
        )
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# ---------------- LOGIN VIEW ----------------
@csrf_exempt
@api_view(['POST'])
def login_view(request):
    email = request.data.get('email', '').strip()
    mot_de_passe = request.data.get('mot_de_passe', '').strip()

    # Ignore la casse sur l'email et prend le premier utilisateur correspondant
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
        return Response({
            "message": "Email ou mot de passe incorrect"
        }, status=status.HTTP_401_UNAUTHORIZED)
