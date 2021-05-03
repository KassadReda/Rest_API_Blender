"""
    BlenderModelSerializer class
    list the fields that the user will see
    by Reda
"""


from .models import BlenderModel

from rest_framework import serializers


class BlenderModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = BlenderModel
        fields = ('name', 'category', 'file')

   