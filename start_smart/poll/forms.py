from django.forms import ModelForm
from django import forms
from .models import Question
from django.contrib.auth.models import User



class PollForm(ModelForm):
    class  Meta:
        model=Question
        fields=['category','question','opt_1','opt_2','opt_3']

class UserProfile(forms.ModelForm):
	

	class Meta():
		model=User
		fields = ['username']

        
    