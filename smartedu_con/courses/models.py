from turtle import mode
from django.db import models

from teachers.models import Teacher

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, null=True, unique=True)
    slug = models.SlugField(null=True, unique=True)
    
    def __str__(self) -> str:
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=50,null=True,unique=True)
    slug=models.SlugField(null=True, unique=True)

    def __str__(self) -> str:
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False,
                            null=False, verbose_name='Kurs Adı', help_text='Kurs Adı Giriniz')
    description = models.TextField(verbose_name='Açıklama',
                                   help_text='Kurs Açıklaması Giriniz', null=False, blank=False)
    teacher= models.ForeignKey(Teacher, null=True,on_delete=models.CASCADE, verbose_name='Eğitmen')
    category=models.ForeignKey(Category, null=True,on_delete=models.DO_NOTHING)
    tags=models.ManyToManyField(Tag,blank=True, null=True)
    image = models.ImageField(
        upload_to='courses/%Y/%m/%d',  default='courses/placeholder-image.jpg')
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(verbose_name='Yayın', default=True)

    def __str__(self):
        return self.name

    
