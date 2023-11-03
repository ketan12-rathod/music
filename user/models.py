from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,date

# Create your models here.
class UserRegister(models.Model):
    address=models.TextField()
    date=models.DateField(default=date.today)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table='user_register'