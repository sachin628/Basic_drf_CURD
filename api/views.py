from django.shortcuts import get_object_or_404, render
from .models import Items
from .serializers import ItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

# Create your views here.
@api_view(['GET'])
def ApiOverview(requests):
    api_urls ={
        'all_items' : '/',
        'Search by Category' :'/?category=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete' : '/Item/pk/delete',
    }

    return Response(api_urls)

# view for inserting item 

@api_view(['POST'])
def add_items(request):
    item = ItemSerializer(data=request.data)

    if Items.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exits')
    
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_items(request):

    if request.query_params:
        items = Items.objects.filter(**request.quey_params.dict())
    else:
        items = Items.objects.all()
    
    if items:
        serializer = ItemSerializer(items,many=True)
        return Response(serializer.data)
    
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['POST'])
def update_items(request, pk):
	item = Items.objects.get(pk=pk)
	data = ItemSerializer(instance=item, data=request.data)

	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_items(request, pk):
	item = get_object_or_404(Items, pk=pk)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTE)
