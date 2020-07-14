from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class finances(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    Expenditure = models.TextField(default="0")
    income = models.TextField(default="0")
    threshold = models.IntegerField(default=0)
    Budget = models.IntegerField(default=0)
    Surplus =  models.IntegerField(default=0)
    transactions = models.TextField(default="")
    def __str__(self):
        return self.user.username