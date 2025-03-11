from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MarketPlaceSerializers
from .models  import MarketPlaceModel
from rest_framework.permissions import IsAuthenticated, IsAdminUser
class CreateMarketPlaceApiView(CreateAPIView):
    serializer_class = MarketPlaceSerializers

class ListMarketPlaceApiView(ListAPIView):
    serializer_class = MarketPlaceSerializers
    queryset = MarketPlaceModel.objects.all()
    permission_classes = (IsAdminUser, )

class UpdateRetrieveDestroyMarketPlaceApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = MarketPlaceSerializers
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        #add user
        return None
    
class GetMyMarketPlace(RetrieveAPIView):
    serializer_class = MarketPlaceSerializers
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        #add user
        return None