from django.shortcuts import render
from forum.forms import UserProfileForm,UserInfo
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
	return render(request,'index.html',{})

@login_required
def special(request):
	return HttpResponse("You are logged in")

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user=authenticate(username=username,password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Account NOT Active")
		else:
			print("someone tried to login and failed")
			print("username: {} and password {}".format(username,password))
			return HttpResponse("invalid login details supplied")
	else:	
		return render(request,'login.html',{})

def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserProfileForm(data=request.POST)
        profile_form = UserInfo(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserProfileForm()
        profile_form = UserInfo()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
