from django.db import models
from django.contrib.auth.models import AbstractUser

class customuser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
    
