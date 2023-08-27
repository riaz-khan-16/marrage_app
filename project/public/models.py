from django.db import models

# Create your models here.




class Intro(models.Model):
    id = models.AutoField(primary_key=True)
    gender =models.CharField(max_length=100)
    mstatus=models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    hometown=models.CharField(max_length=100)
    present_address=models.CharField(max_length=100)
    occupation=models.CharField(max_length=100)
    height=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    blood=models.CharField(max_length=100)

    
class Regi(models.Model):
    phone =models.IntegerField(max_length=100)
    password=models.IntegerField(max_length=100)    


