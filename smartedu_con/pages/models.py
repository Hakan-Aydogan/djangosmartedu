from email import message
from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=11)
    message=models.TextField(max_length=1000)
    date= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name