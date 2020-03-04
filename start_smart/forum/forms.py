from django import forms
from django.contrib.auth.models import User
from forum.models import UserProfileInfo,forum_text,Comment

class UserProfileForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta():
		model=User
		fields = ('username','email','password')

class UserInfo(forms.ModelForm):
	class Meta():
		model = UserProfileInfo
		fields = ('site','profile_pic')

class forumForm(forms.ModelForm):
	class Meta():
		model=forum_text
		fields=('subject','query')


class comment_box(forms.ModelForm):
	class Meta():
		model=Comment
		fields=('desc',)
