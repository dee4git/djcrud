from django.db import models
from django.contrib.auth.models import User
from stores.models import Store


class Product(models.Model):
    name = models.CharField(default="Name", max_length=200)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)
    photo = models.ImageField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
