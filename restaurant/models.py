from django.db import models
from django.utils.timezone import now
# Create your models here.


class Reservation(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateTimeField(default=now)

    def __str__(self):
        return self.name
