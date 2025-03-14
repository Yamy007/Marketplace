from rest_framework.serializers import ModelSerializer
from .models import MarketPlaceModel
from apps.user.serializers import UserSerializer
class MarketPlaceSerializers(ModelSerializer):
    owner = UserSerializer(read_only=True)
    class Meta:
        model = MarketPlaceModel
        fields = ('owner', 'name', 'description', 'slogan', 'image',)

        