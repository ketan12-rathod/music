from django.db import models

# Create your models here.
class Country(models.Model):
    country=models.CharField(max_length=60)

    class Meta:
        db_table='country'