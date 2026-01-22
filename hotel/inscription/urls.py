from django.urls import path, include
from rest_framework import routers
from .views import InscriptionViewSet, login_view

ins_route = routers.DefaultRouter()
ins_route.register(r'ins', InscriptionViewSet, basename='ins')

urlpatterns = [
    path('', include(ins_route.urls)),
    path('login/', login_view, name='login'),
]
