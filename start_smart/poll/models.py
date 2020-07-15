from django.db import models
from django.core.validators import URLValidator
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	

	def __str__(self):
		return self.user.username


class Question(models.Model):
    category=models.CharField(max_length=50)
    question=models.CharField(max_length=100)
    opt_1=models.CharField(max_length=50,)
    opt_2=models.CharField(max_length=50,)
    opt_3=models.CharField(max_length=50,)
    count_opt_1=models.IntegerField(default=0)
    count_opt_2=models.IntegerField(default=0)
    count_opt_3=models.IntegerField(default=0)
    
    name=models.TextField(default=0)
    def __str__(self):
        return self.category
    def total(self):
        return self.count_opt_1+self.count_opt_2+self.count_opt_3    
    




   
    