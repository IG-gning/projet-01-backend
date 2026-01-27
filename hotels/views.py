from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Hotel
from .serializers import HotelSerializer

# GET liste des hôtels
@api_view(['GET'])
@permission_classes([AllowAny])
def listeHotel(request):
    hotels = Hotel.objects.all().order_by('-created_at')
    serializer = HotelSerializer(hotels, many=True, context={'request': request})
    return Response(serializer.data)

# POST ajouter un hôtel
@api_view(['POST'])
@permission_classes([AllowAny])
def addHotel(request):
    serializer = HotelSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
