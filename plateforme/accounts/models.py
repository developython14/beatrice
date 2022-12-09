from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    numero_du_telephone = models.CharField(max_length=100)
    institue = models.CharField(max_length=100)
    def __str__(self):
        return self.name
