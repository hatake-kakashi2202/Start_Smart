from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool
from .models import finances,contact_details,appoint_date
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from math import pi
from django.urls import reverse
import pandas as pd
from django.utils import timezone
from bokeh.io import output_file, show
from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.transform import cumsum
from django.shortcuts import redirect
from django.core.mail import send_mail
import threading
# Create your views here.

def send_reg_mail(email):
	send_mail(email[1],
		email[2],
		'iiits.startsmart@gmail.com',
		[email[0]])

def finance(request):
	return render(request, 'finance.html')

def contact(request):
	if request.method == 'POST':
		if request.POST.get('name') and request.POST.get('email') and request.POST.get('pnumber'):
			model=contact_details()
			model.name= request.POST.get('name')
			model.email = request.POST.get('email')
			model.number = request.POST.get('pnumber')
			model.created_at = timezone.now()
			model.save()
			return HttpResponseRedirect(reverse('finance'))
		else:
			return render(request, 'finance.html', {error:"There was an error in processing, please fill the form again and fill all fields"})

def appointment(request):
	if request.method == 'POST':
		if request.POST.get('slot'):
			model=appoint_date()
			if request.user.is_authenticated:
				model.user = request.user
			else:
				return render(request, 'login.html')
			model.created_at = timezone.now()
			model.slot = request.POST.get("slot")
			model.save()
			return HttpResponseRedirect(reverse('finance'))
		else:
			return render(request, 'finance.html', {error:"There was an error in processing, please fill the form again and fill all fields"})

def graph(request):
	if request.user.is_authenticated:
		try:
			mod = finances.objects.get(user=request.user)
			temp1 = mod.Expenditure[:-1]
			temp2 = mod.income[:-1]
			exp = temp1.split("+")
			tran = temp2.split("+")
			print(exp,tran)
			if exp[0]=="":
				exp[0]=0
			if tran[0]=="":
				tran[0]=0
			else:
				exp =[0]+[int(i) for i in exp]
				tran =[0]+[int(i) for i in tran]
			sum=0
			flag1=0
			flag2=0
			for i in range(0,len(exp)):
				sum+=exp[i]
				if sum > mod.Budget//2 and flag1==0:
					messages.info(request, 'You have completed 50 percent of your budget by month number '+str(i))
					flag1=1
				if sum > mod.Budget and flag2==0:
					messages.info(request, 'You have completed 100 percent of your budget by month number '+str(i))
					flag2=1
				if sum > mod.Budget:
					messages.info(request, 'You have spent rupees '+str(sum-mod.Budget)+' than your budget by month number '+str(i))
			for i in range(1,len(tran)):
				if tran[i]<mod.threshold:
					messages.warning(request, 'Your Income got below the threshold on month '+str(i))
			print(exp,tran)
			index=[]
			for i in range(0,len(exp)+1):
				index.append(i)
			plot = figure(plot_width=800, plot_height=400, title="Trends of Your Expenditure and Income")
			plot.border_fill_color = "whitesmoke"
			plot.min_border_left = 0
			plot.toolbar.autohide = True
			plot.xaxis.axis_label = "Months"
			plot.xaxis.axis_label_text_font_size = "20px"
			plot.xaxis.axis_line_width = 3
			plot.xaxis.axis_line_color = "gray"
			plot.yaxis.axis_label = "Amount"
			plot.yaxis.axis_label_text_font_size = "20px"
			plot.yaxis.axis_line_width = 3
			plot.yaxis.axis_line_color = "gray"
			plot.line(index,exp,color='blue',legend_label="Expenditure")
			plot.line(index,tran,color='green',legend_label="Income")
			plot.line(index,mod.threshold,color='red',legend_label="threshold")
			plot.line(index,mod.Budget,color='black',legend_label="Budget")
			plot.legend.location = "bottom_right"
			plot.legend.label_text_font = "times"
			plot.legend.label_text_font_style = "bold"
			plot.legend.label_text_color = "navy"
			script, div = components(plot)
			details = zip(exp[1:], tran[1:],index[1:-1])
			return render(request,'line.html',{'script':script,'div':div,'details':details,'mod':mod,'index':index[1:-1],'update':True})
		except finances.DoesNotExist:
			plot = figure()
			script, div = components(plot)
			return render(request,'line.html',{'script':script,'div':div,'update':True})
	else:
		return render(request,'login.html',{})

def update_fin(request):
	if request.user.is_authenticated:
		if request.POST.get('expenditure') and request.POST.get('income'):
			try:
				mod = finances.objects.get(user=request.user)
				mod.Expenditure = mod.Expenditure+str(request.POST.get('expenditure'))+"+"
				mod.income = mod.income+str(request.POST.get('income'))+"+"
				mod.save()
			except finances.DoesNotExist:
				mod = finances()
				mod.user = request.user
				mod.Expenditure = request.POST.get('expenditure')+"+"
				mod.income = request.POST.get('income')+"+"
				mod.save()
			return redirect(graph)
		elif request.POST.get('budget') and request.POST.get('threshold'):
			try:
				mod = finances.objects.get(user=request.user)
				mod.threshold = request.POST.get('threshold')
				mod.Budget = request.POST.get('budget')
				mod.save()
				return redirect(graph)
			except finances.DoesNotExist:
				mod = finances()
				mod.user = request.user
				mod.threshold = request.POST.get('threshold')
				mod.Budget = request.POST.get('budget')
				mod.save()
				return redirect(graph)
		else:
			messages.error(request,"Please fill all the fields correctly")
			return redirect(graph)
	else:
		return render(request, 'login.html')	

def update(request):
	if request.POST.get('expenditure') and request.POST.get("income") and request.POST.get('month'):
		try:
			model = finances.objects.get(user=request.user)
			temp1 = model.Expenditure[:-1]
			temp2 = model.income[:-1]
			exp = temp1.split("+")
			tran = temp2.split("+")
			month = int(request.POST.get("month"))-1
			exp[month] = request.POST.get("expenditure")
			tran[month] = request.POST.get('income')
			expenditure = "+".join(exp)+"+"
			income = "+".join(tran)+"+"
			model.Expenditure = expenditure
			model.income = income
			model.save()
			return redirect(graph)
		except finances.DoesNotExist:
			messages.error(request,"Field does not exist")
			return redirect(graph)

	
