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

