from django.db import models

# Create your models here.
from django.db import models
from hotels.models import Hotel

class Entree(models.Model):
    client_nom = models.CharField(max_length=150)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='entrees')
    date_entree = models.DateTimeField(auto_now_add=True)
    date_sortie = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.client_nom} - {self.hotel.nom}"
