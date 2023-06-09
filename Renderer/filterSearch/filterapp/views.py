from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework import status


@api_view(['GET', 'POST'])
def menu_items(request):
    if(request.method=='GET'):
        items = MenuItem.objects.select_related(items, many=True)
        # Searching and filtering
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        # Ordering
        ordering = request.query_params.get('ordering')
        if category_name:
            items = items.filter(category__title=category_name)
        if to_price:
            items = items.filter(price=to_price)
        if search:
            # items = items.filter(title__istartswitch=search)
            items = items.filter(title__icontains=search)
        if ordering:
            # items = items.order_by(ordering)
            ordering_fields = ordering.split(",")
            items = items.order_by(*ordering_fields)
        serialized_item = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data)
    elif request.method == 'POST':
        serialized_item = MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.validated_data, status.HTTP_201_CREATED)

@api_view()
def single_item(request, id):
    item = get_object_or_404(MenuItem, pk=id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)   