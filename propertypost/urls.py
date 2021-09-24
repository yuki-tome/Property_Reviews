from django.urls import path
from .views import PropertyList, PropertyDetail, PropertyCreate, PropertyDelete, PropertyUpdate, SearchPostView

urlpatterns = [
    path('list/', PropertyList.as_view(), name = 'list'),
    path('detail/<int:pk>/', PropertyDetail.as_view(), name = 'detail'),
    path('create/', PropertyCreate.as_view(), name = 'create'),
    path('delete/<int:pk>/', PropertyDelete.as_view(), name = 'delete'),
    path('update/<int:pk>/', PropertyUpdate.as_view(), name = 'update'),
    path('search/', SearchPostView.as_view(), name='search_post'),
]