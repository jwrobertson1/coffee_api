from django.http import JsonResponse
from .models import Coffee
from .serializers import CoffeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def coffee_list(request, format=None):

    if request.method == 'GET':
        coffee = Coffee.objects.all()
        serializer = CoffeeSerializer(coffee, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CoffeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def coffee_detail(request, id, format=None):

    try:
       coffee = Coffee.objects.get(pk=id)
    except Coffee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CoffeeSerializer(coffee)
        return Response(serializer.data)

    elif request.methos == 'PUT':
        serializer= CoffeeSerializer(coffee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        coffee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
