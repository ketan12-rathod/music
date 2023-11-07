from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,date
from myadmin.models import Country
# Create your models here.
class UserRegister(models.Model):
    profile_pic=models.CharField(max_length=255,default=' ')
    date=models.DateField(default=date.today)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table='user_register'
        
# class UserProfile(models.Model):
#     city=models.CharField(max_length=50)
#     gender=models.CharField(max_length=20)
#     dob=models.CharField(max_length=30)
#     marital=models.CharField(max_length=33)
#     age=models.CharField(max_length=33)
#     country=models.ForeignKey(Country,on_delete=models.CASCADE)
#     state=