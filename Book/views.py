from django.shortcuts import render
from rest_framework.response import Response
from .serializers import BookSerializers
from .models import Book
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.


class ApiHomePage(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class ApiDetailPage(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    lookup_field = "id"
