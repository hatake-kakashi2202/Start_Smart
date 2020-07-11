from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
# from django.db.models import CharField, Model
# from django_mysql.models import ListCharField
# Create your models here.

class blog(models.Model):
	title = models.CharField(max_length = 200)
	body = models.TextField()
	writer = models.ForeignKey(User, on_delete = models.CASCADE)
	inter = models.CharField(max_length = 200, default = ' ')
	pub_date = models.DateTimeField(default=datetime.now(), blank=True)
	
	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')