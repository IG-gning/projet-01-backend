from django.db import models

# Create your models here.
from django.db import models

class Hotel(models.Model):
    nom = models.CharField(max_length=150)

    adresse = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
