from django.db import models
from django.contrib.auth.models import User
# Create your models here. 
class Profilepic(models.Model):
    profile=models.FileField(upload_to="Profilepictures" ,max_length=300)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
class Product(models.Model):
    name=models.CharField(max_length=50,unique=True,null=True,blank=True)
    price=models.FloatField(max_length=5,null=True,blank=True)
    def __str__(self):
        return self.name
class Product1(models.Model):
    expirydate=models.DateField(max_length=50,null=True,blank=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
# Create your models here.
