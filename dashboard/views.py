from rest_framework.decorators import api_view

from rest_framework.response import Response
from django.contrib.auth.models import User
from forms_app.models import Formulaire
from messages_app.models import Message
from hotels.models import Hotel
from entrees.models import Entree

@api_view(['GET'])

def dashboard_stats(request):
    data = {
        "formulaires": Formulaire.objects.count(),  # 👈 depuis la base
        "utilisateurs": User.objects.count(),
        "messages": Message.objects.count(),
        "hotels": Hotel.objects.count(),
        "entrees": Entree.objects.count(),
    }
    return Response(data)
