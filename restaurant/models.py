from django.db import models

# Create your models here.


class Reservation(models.Model):
    Name = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateField(auto_now_add=True, null=False, blank=False)
    time = models.TimeField(auto_now=False, null=False, blank=False)