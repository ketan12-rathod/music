from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,date
# Create your models here.
class Contact(models.Model):
    message=models.TextField()
    name=models.CharField(max_length=33)
    email=models.CharField(max_length=100)
    subject=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        db_table='company_contact'
        
class Register(models.Model):
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    date=models.DateField(default=date.today)

    class Meta:
        db_table='company_register'
        
class Add_Song(models.Model):
    s_title=models.CharField(max_length=250)
    s_name=models.CharField(max_length=33)
    m_name=models.CharField(max_length=33)
    mp3=models.CharField(max_length=100)
    img=models.CharField(max_length=255)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(default=date.today)

    class Meta:
        db_table='add_song'
        
class Add_Video(models.Model):
    s_title=models.CharField(max_length=250)
    s_name=models.CharField(max_length=33)
    m_name=models.CharField(max_length=33)
    mp4=models.CharField(max_length=100)
    img=models.CharField(max_length=255)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(default=date.today)

    class Meta:
        db_table='add_video'