from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import  Startup, Mentor
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import smtplib
import random
from datetime import datetime, timedelta, timezone
import threading




# Create your views here.
def signup_sub(request):
	if request.method == 'POST':
		if request.POST['username'] == '':
			return render(request, 'signup.html', {'error':'Input field required'})
		if(request.POST['password1'] == request.POST['password2']):
			try:
				user = User.objects.get(username = request.POST['username'])
				return render(request, 'signup.html', {'error':'username name already exists'})
			except User.DoesNotExist:
				# print(type(request.POST['type']))
				if request.POST['type'] == '1' or request.POST['type'] == '2' or request.POST['type'] == '3':
					user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
					user.email = request.POST['email']
					user.first_name = request.POST['firstname']
					user.last_name = request.POST['lastname']
					new_mentor = Mentor(user = user, person = request.POST['type'])
					new_mentor.save()
					user.save()
					auth.login(request,user)
					return email_auth(request)
				else:
					return render(request, 'signup.html', {'error':'Invalid account type'})
		else: return render(request, 'signup.html', {'error':'passwords doesnot match'})
	else:
		return render(request, 'signup.html')

def signup(request):
	if request.method == 'POST':
		if request.POST['type'] == str(0):
			return signup_startup(request)
		else:
			return signup_sub(request)
	else:
		return render(request, 'signup.html')

def login(request):
	if request.method == 'POST':
		user = auth.authenticate(username = request.POST['username'], password = request.POST['password'])
		if user is not None:
			auth.login(request, user)
			return redirect('index')
		else:
			return render(request, 'login.html', {'error':'Invalid user name or password'})
	else:
		return render(request, 'login.html')

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
	return redirect('index')

def profile(request):
	user = User.objects.get(username = request.user.username)
	try:
		if user.startup is not None:
			is_startup = True
	except:
		is_startup = False
	return render(request, 'profile.html', {'user':user, 'is_startup':is_startup})

def signup_startup(request):
	if request.method == 'POST':
		if(request.POST['password1'] == request.POST['password2']):
			try:
				user = User.objects.get(username = request.POST['username'])
				return render(request, 'signup.html', {'error':'username name already exists'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
				user.email = request.POST['email']
				user.first_name = request.POST['firstname']
				user.last_name = request.POST['lastname']
				k = request.POST['emp_no']
				try:
					k = int(request.POST['emp_no'])
				except ValueError:
					k = 0
				new_startup = Startup(user = user, company_name = request.POST['company_name'], emp_no = k, founder = request.POST['founder'], company_desc = request.POST['company_desc'], head_quarters = request.POST['head_quarters'])
				new_startup.save()
				user.save()
				auth.login(request,user)
				return email_auth(request)
		else:
			return render(request, 'signup.html', {'error':'passwords doesnot match'})
	else:
		return render(request, 'signup.html')

@login_required
def update_info(request):
	user = User.objects.get(username = request.user.username)
	try:
		if user.startup is not None:
			is_startup = True
	except:
		is_startup = False
	return render(request, 'update_info.html', {'user':user, 'is_startup':is_startup})

@login_required
def update_startup(request):
	u = User.objects.get(username = request.user.username)
	u.first_name = request.POST['first_name']
	u.last_name = request.POST['last_name']
	temp_startup = Startup.objects.get(user = u)
	temp_startup.company_name = request.POST['company_name']
	u.email = request.POST['email']
	try:
		k = int(request.POST['emp_no'])
	except ValueError:
		k = 0
	temp_startup.emp_no = k
	temp_startup.founder = request.POST['founder']
	temp_startup.head_quarters = request.POST['head_quarters']
	temp_startup.company_desc = request.POST['company_desc']
	temp_startup.save()
	u.save()
	return redirect('index')

@login_required
def update_user(request):
	u = User.objects.get(username = request.user.username)
	u.first_name = request.POST['first_name']
	u.last_name = request.POST['last_name']
	u.email = request.POST['email']
	u.save()
	return redirect('index')

def send_reg_mail(email):
	send_mail('Congrulations',
		'You have sucessfully registered for Start Smart',
		'startsmart.iiits@gmail.com',
		[email])

@login_required
def email_auth(request):
	u = User.objects.get(username = request.user.username)
	temp_mail = u.email
	mail_thread = threading.Thread(target=send_reg_mail, args=[temp_mail])
	mail_thread.start()
	return redirect('index')
	

def sendmail(list):
	email = list[0]
	rand = list[1]
	send_mail('OTP for reset password',
		'Your OTP for reset password is : ' + str(rand) + '\n\nThe OTP is valid only for 5 minutes.\nDo not share OTP with anyone.',
		'startsmart.iiits@gmail.com',
		[email])

def hash_fun(value):
	return abs(hash(str(value)))

def time_compare(time1, time2):
    temp_time1 = time1.split('_')
    temp_time2 = time2.split('_')
    # print(temp_time1, temp_time2)
    temp_time1 = list(map(int, temp_time1))
    temp_time2 = list(map(int, temp_time2))
    if temp_time1[0] >= temp_time2[0] and temp_time1[1] >= temp_time2[1] and temp_time1[2] >= temp_time2[2] and temp_time1[3] >= temp_time2[3] and temp_time1[4] >= temp_time2[4] and temp_time1[5] >= temp_time2[5]:
    	return True
    else:
    	return False

def time_modify(curr_time):
    curr_time = str(curr_time).split('.')[0]
    curr_time = curr_time.replace('-', '_')
    curr_time = curr_time.replace(':', '_')
    curr_time = curr_time.replace(' ', '_')
    return curr_time

def forget_pass(request):
	if request.method == 'POST':
		# print(request.POST)
		username = request.POST['username']
		if username == '':
			return render(request, 'forget_pass.html', {'error':'Enter the username'})
		try:
			user = User.objects.get(username = username)
		except:
			return render(request, 'forget_pass.html', {'error':'User name does not exist'})
		rand = random.randint(10000, 99999)
		mail_thread = threading.Thread(target=sendmail, args=[[user.email, rand]])
		mail_thread.start()
		
		time_lim = datetime.now(timezone.utc) + timedelta(seconds=300)
		time_lim = time_modify(time_lim)
		rand = hash_fun(rand)
		return redirect('/accounts/verify_pass/' + str(username)+'/'+ str(time_lim)+ '/' + str(rand) )
	return render(request, 'forget_pass.html')

def verify_pass(request, username, time_lim, rand):
	if request.method == 'POST':
		otp = request.POST['otp']
		if otp == '':
			return render(request, 'verify_pass.html', {'error':'OTP cannot be None'})
		otp = int(otp)
		curr_time = datetime.now(timezone.utc)
		curr_time = time_modify(curr_time)
		if time_compare(curr_time, time_lim):
			return render(request, 'verify_pass.html', {'error':'OTP expired'})
		otp = hash_fun(otp)
		# print(rand, otp)
		if str(otp) == str(rand):
			# return render(request, 'new_pass.html', )
			return redirect('/accounts/new_pass/' + username+'/' + str(otp))
		else:
			return render(request, 'verify_pass.html', {'error':'Invalid OTP'})
	else:
		return render(request, 'verify_pass.html')

def new_pass(request, username, password):
	# print(username, password)
	if request.method == 'POST':
		
		pass1 = request.POST['password1']
		pass2 = request.POST['password2']
		if pass1 != pass2:
			return render(request, 'new_pass.html', {'error':'Both passwords doesnot match'})
		else:
			user = User.objects.get(username = username)
			user.set_password(pass1)
			user.save()
			user = User.objects.get(username = username)
			return redirect('index')
	else:
		return render(request, 'new_pass.html' , {'temp_username':username})