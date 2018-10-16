from django.db import models
# Create your models here.


class AwardNominee(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    imgname = models.CharField(max_length=100)
    currvotes = models.PositiveIntegerField()

