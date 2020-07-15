from django.shortcuts import render,redirect,HttpResponse
from .models import Question
from .forms import PollForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from poll.models import UserProfile
# Create your views here.
def home(request):
    poll=Question.objects.all()

    context={
        'poll':poll,
    }
    return render(request,'home.html',context)




def creat(request):
    if request.method == 'POST':
        form=PollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=PollForm(request.POST)
        context={
            'form':form,
        }
        return render(request,'creat.html',context)        

    context={
        'form':form,
    }
    return render(request,'creat.html',context)
@login_required
def vote(request,poll_id):
    poll=Question.objects.get(pk=poll_id)
    
    if request.method == 'POST':
        sel_opt=request.POST['poll']
        model=UserProfile()
        model.user=request.user
        print(model.user)
        if sel_opt == 'option1' :
            poll.count_opt_1 += 1
        elif sel_opt == 'option2':
            poll.count_opt_2 += 1 
        elif sel_opt == 'option3' :
            poll.count_opt_3 += 1
        else :
            return HttpResponse(400,'Invalid vote form')
        names=str(model.user)
          
        poll.name +=str(model.user)
        print(poll.name)
        if  Question.objects.filter(pk=poll_id,name__icontains=names):
            
            return HttpResponse("<h3>You are already voted for this please go back to answer  the next question .</h3>")
        else:  
            
            poll.name +=names
            poll.save()  
        return redirect('home')                
        
       
    

    context={
        'poll':poll
    }

    return render(request,'vote.html',context)

def result(request,poll_id):
    poll=Question.objects.get(pk=poll_id)
    try:
        per1=poll.count_opt_1/poll.total()*100
        per2=poll.count_opt_2/poll.total()*100
        per3=poll.count_opt_3/poll.total()*100
    except ZeroDivisionError as error:
        return HttpResponse("<h1>no vote yet</h1>")
    context={
         'poll':poll,
         'per1':per1,
         'per2':per2,
         'per3':per3,
         
    }
    return render(request,'result.html',context)        


