from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to='static/image/',null=True,blank=True)
    
    def __str__(self):
        return self.name
    
class item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100,null=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='static/image/',null=True,blank=True)
    
    def __str__(self):
        return self.name
