from django.db import models



class MarketPlaceModel(models.Model):
    class Meta:
        db_table = 'marketplace'
    

    name = models.CharField(unique=True, max_length=25)
    description = models.CharField(max_length=255)
    slogan = models.CharField(max_length=25)
    image = models.ImageField(upload_to='marketplace/', blank=True, null=True)


