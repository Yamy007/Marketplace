from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MarketPlaceSerializers
from .models  import MarketPlaceModel
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
class CreateMarketPlaceApiView(CreateAPIView):
    serializer_class = MarketPlaceSerializers
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        user = self.request.user
        data = self.request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner = user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
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
        user = self.request.user 
        return MarketPlaceModel.objects.filter(owner = user).first()
