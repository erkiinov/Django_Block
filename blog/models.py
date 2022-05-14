from distutils.command.upload import upload
from email.mime import image
from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class post(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/") 
    choose = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

