from django.shortcuts import render
from .serializers import ProductSerializers
from .models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def product_list(request):
    products=Product.objects.all()
    serializer=ProductSerializers(products,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createProduct(request):
   serializer=ProductSerializers(data=request.data)
   if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)