from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager
class ProfileModel(models.Model):
    class Meta:
        db_table ="profile_users"
    
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    age = models.IntegerField(default=18)
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)


class UserModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = "auth_users"
    
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)




    #permission
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)


    #profile
    profile = models.OneToOneField(ProfileModel, on_delete=models.CASCADE, related_name='user')
    USERNAME_FIELD = "email"
    objects = UserManager()