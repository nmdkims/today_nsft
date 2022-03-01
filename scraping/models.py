from django.db import models


# Create your models here.
class Climate(models.Model):
    region = models.CharField(max_length=30, blank=True, null=True)
    weather = models.CharField(max_length=30, blank=True, null=True)
    h_temp = models.CharField(max_length=30, blank=True, null=True)
    l_temp = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'climate'
