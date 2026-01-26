from django.urls import path
from .views import dashboard_stats

urlpatterns = [
    path('api/dashboard/', dashboard_stats),
]
