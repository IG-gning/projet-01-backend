from django.urls import path
from .views import listeHotel, addHotel

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('listeHotel/', listeHotel, name='listeHotel'),
    path('addHotel/', addHotel, name='addHotel'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
