from django import forms
from django.contrib.auth.models import User
from contacts.models import errordetect


class errorForms(forms.ModelForm):
	class Meta():
		model=errordetect
		fields=('query',)

