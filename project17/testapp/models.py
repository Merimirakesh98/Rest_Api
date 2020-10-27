from django.db import models

# Create your models here.

class Student(models.Model):
	sno = models.IntegerField()
	sname = models.CharField( max_length=50)
	sphono = models.IntegerField()
	saddress = models.CharField( max_length=50)