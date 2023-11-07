from django.db import models

# Create your models here.
class Country(models.Model):
    country=models.CharField(max_length=60)

    class Meta:
        db_table='country'

class State(models.Model):
    state=models.CharField(max_length=255)
    country=models.ForeignKey(Country,on_delete=models.CASCADE)

    class Meta:
        db_table='state'