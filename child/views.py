from django.shortcuts import render
from .models import Child
from .serializers import ChildSerializer

from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class ChildView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        pass

    def post(self, request, format=None, *args, **kwargs):
        pass

    def put(self, request, pk, format=None, *args, **kwargs):
        pass

    def delete(self, request, pk, format=None, *args, **kwargs):
        pass
