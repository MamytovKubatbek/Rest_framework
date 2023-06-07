
from django.urls import path
from . import views
# from .views import *

urlpatterns = [
    path('productsList/', views.ProductsAPIList.as_view(), name="ProductsList"),
    path('brandList/', views.BrandAPIList.as_view(), name="BrandList"),
    
    path('cartsList/', views.CartAPIList.as_view(), name="CartsList"),
    path('cartsList/<int:pk>/', views.CartList.as_view(), name="CartsList"),

    path('orderList/', views.OrderAPIList.as_view(), name="OrderList"),
    path('orderList/<int:pk>/', views.OrderList.as_view(), name="OrderList"),
   
    path('commentList/', views.CommentAPIList.as_view(), name="CommentList"),
]
