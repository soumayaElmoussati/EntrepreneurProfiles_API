from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Subscription(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class EntrepreneurProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    description = models.TextField()
    sector = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True)
    telephone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


