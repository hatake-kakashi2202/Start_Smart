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
	# user = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE)
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	subject=models.CharField(max_length=264)
	query=models.TextField()
	liked = models.ManyToManyField(User,default=None,blank=True,related_name='liked')
	created_at = models.DateTimeField(auto_now_add=True)
	views = models.IntegerField(default=0)

	def __str__(self):
		return self.subject

	@property
	def num_likes(self):
		return self.liked.all().count()

Like_Choices = (
	('Like',"Like"),
	('Unlike','Unlike')
)

class Like(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	post = models.ForeignKey(forum_text,on_delete=models.CASCADE)
	value =models.CharField(choices=Like_Choices,default='Like',max_length=10)

	def __str__(self):
		return str(self.post)


class Comment(models.Model):
    # user = models.ForeignKey(UserProfileInfo,on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    forum = models.ForeignKey(forum_text, on_delete=models.CASCADE)
    desc = models.TextField(default='SOME STRING')
    created_at = models.DateTimeField(auto_now_add=True)

