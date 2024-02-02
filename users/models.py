from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
# Create your models here.

class CustomUser(AbstractUser):
    phone_number=models.CharField(max_length=13)
    image=models.ImageField(default='users_image/user_default_image.png',upload_to='media/users_image')

    def __str__(self):
        return  self.username

    class Meta:
        db_table='users_table'
