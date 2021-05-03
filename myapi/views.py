"""
    class BlenderViewSet
    this class define how to display a model.
    by Reda
"""
# coding=utf-8
from django.shortcuts import render
from rest_framework import viewsets

from .serializers import BlenderModelSerializer
from .models import BlenderModel
# Create your views here.


class BlenderViewSet(viewsets.ModelViewSet) : 
    queryset = BlenderModel.objects.all().order_by('name')
    serializer_class = BlenderModelSerializer
    

    #serialise the uploaded file
    def file(self, request,pk=None) : 
        blenderModel= self.get_object()
        file = blenderModel.file
        serializer = BlenderModelSerializer(file, data=request.data)