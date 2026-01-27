from django.db import models
from cloudinary.models import CloudinaryField

class Hotel(models.Model):
    nom = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    prix = models.IntegerField(default=0)
    adresse = models.CharField(max_length=200)
    image = CloudinaryField('image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
