from rest_framework.serializers import ModelSerializer
from .models import MarketPlaceModel

class MarketPlaceSerializers(ModelSerializer):
    class Meta:
        db_table = 'marketplace'
    model = MarketPlaceModel
    fields = "__all__"

    