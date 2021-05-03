"""
    this file contains what database can we modify from the admin panel
"""

from django.contrib import admin
from .models import BlenderModel
# Register your models here.

admin.site.register(BlenderModel)
