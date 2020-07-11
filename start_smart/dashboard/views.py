from django.shortcuts import render

# Create your views here.
def dashboard(request):
	return render(request, 'project.html')

def extend(request):
	return render(request, 'extend.html')