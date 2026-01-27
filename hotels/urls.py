from django.urls import path
from .views import listeHotel, addHotel

urlpatterns = [
    path('listeHotel/', listeHotel, name='listeHotel'),
    path('addHotel/', addHotel, name='addHotel'),
]
