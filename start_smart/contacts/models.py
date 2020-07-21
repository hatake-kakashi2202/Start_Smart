from django.db import models
from django.core.validators import URLValidator
from django.contrib.auth.models import User




class errordetect(models.Model):
	
	query=models.TextField()
	

	def __str__(self):
		return self.query

    


