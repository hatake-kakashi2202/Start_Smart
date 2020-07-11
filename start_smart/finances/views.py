from django.shortcuts import render

# Create your views here.
def finance(request):
	return render(request, 'finance.html')