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
    hotels = Hotel.objects.all()
    serializer = HotelSerializer(hotels, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def addHotel(request):
    print("Data reçue :", request.data)
    serializer = HotelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        print("Erreur serializer :", serializer.errors)
        return Response(serializer.errors, status=400)

