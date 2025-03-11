from django.urls import path
from .views import GetMyMarketPlace, UpdateRetrieveDestroyMarketPlaceApiView, CreateMarketPlaceApiView, ListMarketPlaceApiView
urlpatterns = [
    path('create/', CreateMarketPlaceApiView.as_view(), name="create_marketplace"),
    path('marketplace/', UpdateRetrieveDestroyMarketPlaceApiView.as_view(), name="update_retrieve_destroy_marketplace"),
    path('my/', GetMyMarketPlace.as_view(), name="get_my_marketplace"),
    path('list/', ListMarketPlaceApiView.as_view(), name="list_marketplace"),
]
