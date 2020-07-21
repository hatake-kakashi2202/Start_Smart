from django.db import models
from django.contrib.auth.models import User

# class Client(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	company_name = models.CharField(max_length = 20)

# Create your models here.
class Startup(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	company_name = models.CharField(max_length = 30)
	emp_no = models.IntegerField(default = 0, blank  = True)
	founder = models.CharField(max_length = 30, blank = True)
	company_desc = models.CharField(max_length = 200, blank = True)
	head_quarters = models.CharField(max_length = 200, blank = True)
	profile_pic = models.ImageField(upload_to='profile_pics',blank=True)



class Mentor(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	# 1 - Mentor , 2 - indivudal, 3 - Corporate
	person = models.IntegerField(default = 0)
	profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

class Fields(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	is_email_verified = models.BooleanField(default=False)