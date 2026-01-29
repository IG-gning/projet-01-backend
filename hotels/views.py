from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Hotel
from .serializers import HotelSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def listeHotel(request):
    hotels = Hotel.objects.all().order_by('-created_at')
    serializer = HotelSerializer(hotels, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def addHotel(request):
    serializer = HotelSerializer(data=request.data)

    if serializer.is_valid():
        hotel = serializer.save()
        return Response(HotelSerializer(hotel).data, status=201)

    return Response(serializer.errors, status=400)
