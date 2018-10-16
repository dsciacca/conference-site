from django.db import models

# Create your models here.


class Workshop(models.Model):
    sessionchoices = (('1', '1'), ('2', '2'), ('3', '3'))
    title = models.CharField(max_length=50)
    session = models.CharField(choices=sessionchoices, max_length=1)
    roomnumber = models.CharField(max_length=10)
    starttime = models.CharField(max_length=10)
    endtime = models.CharField(max_length=10)
