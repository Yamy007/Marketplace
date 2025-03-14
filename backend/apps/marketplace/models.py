from django.db import models
from apps.user.serializers import UserModel


class MarketPlaceModel(models.Model):
    class Meta:
        db_table = 'marketplace'
    
    owner = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='marketplace')
    name = models.CharField(unique=True, max_length=25)
    description = models.CharField(max_length=255)
    slogan = models.CharField(max_length=25)
    image = models.ImageField(upload_to='marketplace/', blank=True, null=True)


