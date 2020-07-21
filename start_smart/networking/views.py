from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def mentor(request):
	mentors = []
	count = 0
	for x in User.objects.all():
		try:
			if x.mentor is not None and x.mentor.person == 1:
				if count % 3 == 0:
					mentors.append([1, x])
				elif (count + 1) % 3 == 0:
					mentors.append([x, 2])
				else:
					mentors.append([x])
				count += 1
		except:
			print('', end='')
	if count % 3 != 0:
		mentors.append([2])
	return render(request, 'connectWithMentors.html', {'mentors':mentors})

def incubators(request): # for now it is corporate
	corps = []
	count = 0
	for x in User.objects.all():
		try:
			if x.mentor is not None and x.mentor.person == 3:
				if count % 3 == 0:
					corps.append([1, x])
				elif (count + 1) % 3 == 0:
					corps.append([x, 2])
				else:
					corps.append([x])
				count += 1
		except:
			print('', end='')
	if count % 3 != 0:
		corps.append([2])
	return render(request, 'connectWithIncubators.html', {'corps':corps})

def student(request):
	starts = []
	count = 0
	for x in User.objects.all():
		try:
			if x.startup is not None:
				if count % 3 == 0:
					starts.append([1, x])
				elif (count + 1) % 3 == 0:
					starts.append([x, 2])
				else:
					starts.append([x])
				count += 1
		except:
			print('', end='')
	if count % 3 != 0:
		starts.append([2])
	return render(request, 'connectWithStudents.html', {'starts':starts})
