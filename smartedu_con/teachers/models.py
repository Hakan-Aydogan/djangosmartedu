from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Teacher(models.Model):
    name= models.CharField(max_length=50)
    title= models.CharField(max_length=50)
    description=models.TextField(max_length=1500,null=True)
    image = models.ImageField(
        upload_to='teachers/%Y/%m/%d',  default='courses/placeholder-image.jpg')
    facebook=models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    linkedin= models.URLField(blank=True)
    twitter= models.URLField(blank=True)
    
    def __str__(self):
        return self.name