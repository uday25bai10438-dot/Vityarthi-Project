from django.db import models

class Product(models.Model):
      Name = models.CharField(max_length=200)
      Price = models.IntegerField()
      Stock = models.IntegerField()
      Image_Url = models.CharField(max_length=2085)

class offer(models.Model):
    code= models.CharField()
    description = models.CharField()
    discount=models.FloatField()

