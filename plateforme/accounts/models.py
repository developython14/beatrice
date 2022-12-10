from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class Profile(AbstractUser):
    nom = models.CharField(max_length=100 ,null=False )
    prenom = models.CharField(max_length=100,null=False )
    email = models.CharField(max_length=100,unique=True,default='khasarou@gmail.com')
    password = models.CharField(max_length=100 )
    numero_du_telephone = models.CharField(max_length=100,null=False )
    institue = models.CharField(max_length=100,null=False )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['prenom', 'institue' , 'password']
    def __str__(self):
        return self.nom
