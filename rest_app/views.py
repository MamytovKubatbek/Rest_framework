from django.shortcuts import render

from .models import *
from .serializer import *
from rest_framework import generics , mixins

from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticated


# Create your views here.

class ProductsPagination(PageNumberPagination):
    page_size = 1

    page_size_query_param = 'page_size'

    max_page_size = 10000

class ProductsAPIList(generics.ListAPIView):

    queryset = Products.objects.all()
    serializer_class = ProductsSerializers
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('name', 'descriptions', 'size')

    pagination_class = ProductsPagination

class BrandAPIList(generics.ListAPIView):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializers



class CartAPIList(generics.ListAPIView, mixins.CreateModelMixin , GenericAPIView):

    queryset = Cart.objects.all()
    serializer_class = CartSerializers
    permission_classes = [IsAuthenticated]


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class CartList(generics.ListAPIView, mixins.RetrieveModelMixin , mixins.UpdateModelMixin, mixins.DestroyModelMixin , GenericAPIView):

    queryset = Cart.objects.all()
    serializer_class = CartSerializers
    permission_classes = [IsAuthenticated]


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class OrderAPIList(generics.ListAPIView, mixins.CreateModelMixin , GenericAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)




class OrderList(generics.ListAPIView, mixins.RetrieveModelMixin , mixins.DestroyModelMixin , GenericAPIView):

    queryset = Cart.objects.all()
    serializer_class = CartSerializers
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class CommentAPIList(generics.ListAPIView, mixins.CreateModelMixin , GenericAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializers


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CommentList(generics.ListAPIView, mixins.RetrieveModelMixin , mixins.DestroyModelMixin , GenericAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

