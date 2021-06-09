from django.db import models
from django.shortcuts import render
from django.http import Http404
from rest_framework import serializers, status
from .models import Child
from .serializers import ChildSerializer

from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class ChildView(APIView):
    serializer_class = ChildSerializer
    model = Child
    
    def get_child(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return Http404
        
    def get(self, request, format=None, *args, **kwargs):
        children = self.model.objects.all()
        serializers = self.serializer_class(children, many=True)
        return Response(serializers.data)

    def post(self, request, format=None, *args, **kwargs):
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None, *args, **kwargs):
        child = self.get_child(pk)
        serializers = self.serializer_class(child, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        child = self.get_child(pk)
        child.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)


class SingleChild(APIView):
    def get(self, request, format=None, *args, **kwargs):
        pass