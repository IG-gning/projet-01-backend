from django.urls import path
from .views import InscriptionViewSet, login_view

inscription_register = InscriptionViewSet.as_view({'post': 'register'})

urlpatterns = [
    path('register/', inscription_register, name='register'),
    path('login/', login_view, name='login'),
]
