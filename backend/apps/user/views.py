from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .serializers import UserSerializer, UserModel
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class CreateUserAPiView(CreateAPIView):
    serializer_class = UserSerializer

class GetUserApiView(ListAPIView):
    permission_classes= (IsAdminUser,)
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

class RetrieveUpdateDestroyUserApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )
    
    def get_object(self):
        return self.request.user
    
class GetMeApiView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user