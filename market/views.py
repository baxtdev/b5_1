from django.shortcuts import render
from rest_framework import status,permissions 

from rest_framework.views import APIView
from rest_framework.decorators import api_view

from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Category
from .serializers import CategorySerializer



class CategoryListApiView(APIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        qs = self.get_queryset()
        serializer = self.get_serializer(qs, many=True)  
        return Response(serializer.data, status=200)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  
        return Response(serializer.errors, status=400)



class CategoryDetailApiView(APIView):
    serializer_class = CategorySerializer

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return None

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)

    def get(self, request, pk, *args, **kwargs):
        category = self.get_object(pk)
        if category is None:
            return Response({"detail": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(category)
        return Response(serializer.data, status=200)

    def put(self, request, pk, *args, **kwargs):
        category = self.get_object(pk)
        if category is None:
            return Response({"detail": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(category, data=request.data, partial=True)  # partial=True для частичного обновления
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
