from django.shortcuts import render
from django.http import Http404
from .models import Sponser
from .serializers import SponserSerializer

# rest dependencies import
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class AllSponsers(APIView):
    model = Sponser
    serializer = SponserSerializer

    def get(self, request, format=None, *args, **kwargs):
        sponser = self.model.objects.all()
        serializer = self.serializer(sponser, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        sponser_data = serializer.data

        response = {
            'data': {
                'sponser': dict(sponser_data),
                'status': 'success',
                'sponser': 'Sponser has been added successfully'
            }
        }

        return Response(response, status=status.HTTP_201_CREATED)


class SingleSponser(APIView):
    model = Sponser
    serializer = SponserSerializer

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None, *args, **kwargs):
        sponser = self.get_object(pk)
        serializer = self.serializer(sponser)

        return Response(serializer.data)

    def put(self, request, pk, format=None, *args, **kwargs):
        sponser = self.get_object(pk)
        serializer = self.serializer(sponser, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        sponser = self.get_object(pk)
        sponser.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
