from django.db import models


class Car(models.Model):
    mark = models.CharField(max_length=20)
    producer = models.CharField(max_length=20)
    year = models.IntegerField()
    num = models.CharField(max_length=20)

