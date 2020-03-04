from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class UserProfileInfo(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	site = models.URLField(blank=True)
	profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

	def __str__(self):
		return self.user.username

class forum_text(models.Model):
	user = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE)
	subject=models.CharField(max_length=264)
	query=models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.subject


class Comment(models.Model):
    user = models.ForeignKey(UserProfileInfo,on_delete=models.CASCADE)
    forum = models.ForeignKey(forum_text, on_delete=models.CASCADE)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)