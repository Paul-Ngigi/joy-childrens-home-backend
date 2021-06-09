from django.shortcuts import render
from django.http import Http404
from .models import Child
from .serializers import ChildSerializer

# rest dependencies import
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class AllChildren(APIView):
    model = Child
    serializer = ChildSerializer

    def get(self, request, format=None, *args, **kwargs):
        children = self.model.objects.all()
        serializer = self.serializer(children, many=True)

        return Response(serializer.data)

    def post(self, request, format=None, *args, **kwargs):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleChild(APIView):
    model = Child
    serializer = ChildSerializer

    def get_object(self, request, pk, format=None, *args, **kwargs):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None, *args, **kwargs):
        child = self.get_object(pk)
        serializer = self.serializer(child)

        return Response(serializer.data)

    def put(self, request, pk, format=None, *args, **kwargs):
        child = self.get_object(pk)
        serializer = self.serializer(child, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        child = self.get_object(pk)
        child.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
