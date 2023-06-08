from django.db import models

# Create your models here.
class Task(models.Model):
     num= models.IntegerField()
     name=models.CharField(max_length=250)
     decription=models.CharField(max_length=250)

     def __str__(self):
         return self.name