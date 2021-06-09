from django.shortcuts import render
from django.http import Http404
from .models import Adopter
from .serializers import AdopterSerializer

# rest dependencies import
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class AllAdopters(APIView):
    model = Adopter
    serializer = AdopterSerializer

    def get(self, request, format=None, *args, **kwargs):
        adopter = self.model.objects.all()
        serializer = self.serializer(adopter, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        adopter_data = serializer.data

        response = {
            'data': {
                'adopter': dict(adopter_data),
                'status': 'success',
                'adopter': 'Adopter has been added successfully'
            }
        }

        return Response(response, status=status.HTTP_201_CREATED)


class SingleAdopter(APIView):
    model = Adopter
    serializer = AdopterSerializer

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None, *args, **kwargs):
        adopter = self.get_object(pk)
        serializer = self.serializer(adopter)

        return Response(serializer.data)

    def put(self, request, pk, format=None, *args, **kwargs):
        adopter = self.get_object(pk)
        serializer = self.serializer(adopter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        adopter = self.get_object(pk)
        adopter.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
