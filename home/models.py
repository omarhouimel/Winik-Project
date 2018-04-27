from django.db import models

# Create your models here.
class GaleriePhoto(models.Model):
    image=models.ImageField(upload_to='image/')
    title=models.CharField(max_length=30,default="title")

    def __str__(self):
        return self.title

class Contact(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30,default="omar@gmail0com")
    user_name = models.CharField(max_length=30,default='omar')
    password = models.CharField(max_length=30,default=" ")

    def __str__(self):
        return self.full_name
class Position (models.Model):
    lat=models.CharField(max_length=20)
    lng=models.CharField(max_length=20)
    place=models.CharField(max_length=20,default='Tunis')

    def __str__(self):
      return  self.place







