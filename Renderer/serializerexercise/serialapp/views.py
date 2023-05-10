from django.shortcuts import render
from .models import MenuItem
from .serializers import MenuItemsSerializer
from rest_framework import generics
# Create your views here.


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemsSerializer
   
   
class SingleMenuItemsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemsSerializer