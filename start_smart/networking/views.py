from django.shortcuts import render

# Create your views here.
def mentor(request):
	return render(request, 'connectWithMentors.html')

def incubators(request):
	return render(request, 'connectWithIncubators.html')

def student(request):
	return render(request, 'connectWithStudents.html')
