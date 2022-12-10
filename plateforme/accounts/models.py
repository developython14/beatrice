from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Profile(AbstractUser):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100 )
    email = models.CharField(max_length=100,unique=True,null=True)
    password = models.CharField(max_length=100,default='12345678')
    numero_du_telephone = models.CharField(max_length=100,unique=True )
    institue = models.CharField(max_length=100 )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.nom
