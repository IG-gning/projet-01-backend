from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def dashboard_stats(request):
    data = {
        "formulaires": 125,
        "messages": 40,
        "utilisateurs": 600,
        "emails": 25,
        "hotels": 40,
        "entrees": 0
    }
    return Response(data)
