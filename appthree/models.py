from django.db import models
from apptwo.models import Car
from appone.models import Model


# Create your models here.


class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.pk)