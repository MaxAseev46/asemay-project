from django.db import models

# Create your models here.

class Course(models.Model): 
    name = models.CharField(max_length=30) 
 
class Student(models.Model):     
    name = models.CharField(max_length=30)     
    courses = models.ManyToManyField(Course) 

class User(models.Model): 
    name = models.CharField(max_length=20) 
 
class Account(models.Model):     
    login = models.CharField(max_length=20)     
    password = models.CharField(max_length=20) 
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True) 
