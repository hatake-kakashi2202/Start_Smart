from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class finances(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    Expenditure = models.TextField(default="0")
    income = models.TextField(default="0")
    threshold = models.IntegerField(default=0)
    Budget = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username

class contact_details(models.Model):
    name = models.CharField(max_length=264)
    email = models.EmailField(max_length=254)
    number = models.CharField(max_length=13)
    STATUS_CHOICES = (
    ('open','OPEN'),
    ('waiting', 'WAITING'),
    ('closed','CLOSED'),
    )
    status = models.CharField(max_length = 20, choices=STATUS_CHOICES,default='open')
    created_at = models.DateTimeField()
    def __str__(self):
        return self.name

class appoint_date(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    slot = models.DateTimeField()
    STATUS_CHOICES = (
    ('open','OPEN'),
    ('closed','CLOSED'),
    )
    status = models.CharField(max_length = 20, choices=STATUS_CHOICES,default='open')
    def __str__(self):
        return self.user.username+" at " + str(self.slot)
