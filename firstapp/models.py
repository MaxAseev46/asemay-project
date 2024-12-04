from django.db import models

# Create your models here.

class Course(models.Model): 
    name = models.CharField(max_length=30) 
 
class Student(models.Model):     
    name = models.CharField(max_length=30)     
    courses = models.ManyToManyField(Course) 

class Person(models.Model): 
    name = models.CharField(max_length=20,
                            verbose_name="Имя клиента") 
    age = models.IntegerField(verbose_name="Возраст клиента")     
    object_person = models.Manager() 
    DoesNotExist = models.Manager 
 
class Company(models.Model): 
    name = models.CharField(max_length=30) 

class Product(models.Model): 
    company = models.ForeignKey(Company, on_delete=models.CASCADE)     
    name = models.CharField(max_length=30) 
    price = models.IntegerField() 

class User(models.Model):
    name = models.CharField(max_length=20)

class Account(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True)
    
class Image(models.Model):
 title = models.CharField(max_length=100, null=False,
 verbose_name="Описание изображения",)
 image = models.ImageField(upload_to='images',
 verbose_name="Файл с изображением",
 null=True, blank=True)
 obj_img = models.Manager()
 
 def __str__(self):
    return self.title