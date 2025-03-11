from django.urls import path
from .views import CreateUserAPiView, GetUserApiView, RetrieveUpdateDestroyUserApiView, GetMeApiView

urlpatterns = [
    path('create/', CreateUserAPiView.as_view(), name="create_user"),
    path('me/', GetMeApiView.as_view(), name="get_me"),
    path('list/', GetUserApiView.as_view(), name="list_user"),
    path('user/', RetrieveUpdateDestroyUserApiView.as_view(), name="retrieve_update_destroy"),
]