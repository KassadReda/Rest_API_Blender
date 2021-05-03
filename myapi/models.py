"""
    class BlenderModel
    by Reda
"""

from django.db import models

# Create your models here.

class BlenderModel(models.Model):
    #id = models.AutoField()
    name = models.CharField(max_length = 60)
    category = models.CharField(max_length = 60)
    #example : file will be saved to MEDIA_ROOT/uploads/2020/11/03
    file = models.FileField('Contract file (Blend)',upload_to='uploads/%Y/%m/%d/', max_length=100,blank=False, null=False)
    #display the name of the model
    def __str__(self):
        return self.name