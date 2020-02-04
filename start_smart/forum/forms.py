from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserProfileForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta():
		model=User
		fields = ('username','email','password')

class UserInfo(forms.ModelForm):
	class Meta():
		model = UserProfileInfo
		fields = ('site','profile_pic')
