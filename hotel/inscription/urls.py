from django.urls import path, include
from rest_framework import routers
from .views import InscriptionViewSet, login_view

router = routers.DefaultRouter()
router.register(r'ins', InscriptionViewSet, basename='ins')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_view, name='login'),
]
