
from django.db import models
# Create your models here.
import datetime



class profile(models.Model):
    name=models.CharField(("name"), max_length=50)
    email=models.EmailField(("email"), max_length=254)
    school=models.CharField(("school"), max_length=50)
    skill=models.TextField(("skill"),max_length=100)
    about=models.TextField(("about"),max_length=500)
    acherviment=models.TextField(("acherviment"),max_length=1000)
    acherviment1=models.TextField(("acherviment1"),max_length=1000,default="")
    web=models.TextField(("web"),max_length=1000,default="")
    number=models.CharField(("number"),max_length=10)
    previous_work=models.CharField(("previous_work"),max_length=500,default="")
    high=models.CharField(("high"),max_length=500,default="")
    sec=models.CharField(("sec"),max_length=500,default="")
    branch=models.CharField(("branch"),max_length=500,default="")
    CGPA=models.CharField(("CGPA"),max_length=500,default="")
    link=models.CharField(("link"),max_length=500,default="")
    coding=models.CharField(("coding"),max_length=500,default="")
    #img=models.ImageField(("img"), upload_to=None, height_field=2, width_field=1, max_length=2)
      

    def __str__(self):
        return self.name + self.email