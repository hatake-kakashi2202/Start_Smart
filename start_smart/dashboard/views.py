from django.shortcuts import render

# Create your views here.
def dashboard(request):
	return render(request, 'dashboardmainpage.html')

def startupandCoorporate(request):
	return render(request, 'startupandCoorporate.html')

def Individual(request):
	return render(request, 'Individual.html')

def Mentors(request):
	return render(request, 'Mentors.html')
