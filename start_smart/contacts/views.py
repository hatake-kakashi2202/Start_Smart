from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from contacts.models import  errordetect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from contacts.forms import errorForms
import smtplib
import random
from datetime import datetime, timedelta, timezone
import threading
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse



def index(request):
	return render(request,'index.html',{})



@login_required
def comment(request):
    form=errorForms()
    mod = errordetect.objects.all()
    if request.method == 'POST':
        
        if request.POST['username'] == '':
            return render(request, 'contactus.html', {'error':'Input field required'})
        try:
            
            user = User.objects.get(username = request.POST['username'])
        
        
            if request.POST.get('query'):
                model=errordetect()
                print(request.POST['username'])
                model.query = request.POST.get('query')
                model.save()
                return email_auth(request)
            else:
                return render(request, 'contactus.html', {})
        except User.DoesNotExist:
            
            return render(request, 'contactus.html', {'error':'Enter valid username'})
    else:
        return render(request, 'contactus.html', {'form': form,'mod':mod})

@login_required
def email_auth(request):
	u = User.objects.get(username = request.user.username)
	temp_mail = u.email 
    
	mail_thread = threading.Thread(target=send_reg_mail, args=[temp_mail])

	mail_thread.start()
    
	return redirect('index')


def send_reg_mail(email):
    
	send_mail('Thank you for your query',
		'Our team will look into it and solves the problem as soon as possible',
		'startsmart.iiits@gmail.com',
		[email])




