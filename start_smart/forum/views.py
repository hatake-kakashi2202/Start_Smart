from django.shortcuts import render
from forum.forms import UserProfileForm,UserInfo,forumForm,comment_box
from forum.models import forum_text,UserProfileInfo,Comment,Like
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
import uuid
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from accounts.models import Startup,Mentor
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from copy import deepcopy

# Create your views here.


def index(request):
	return render(request,'index.html',{})

def finances(request,user_name='pkashyap'):
	return render(request,'finances.html',{'user_name':user_name})

def forum(request):
    mod_list = forum_text.objects.all().order_by('-id')
    paginator = Paginator(mod_list, 5)
    page_number = request.GET.get('page')
    mod = paginator.get_page(page_number)
    pic = User.objects.all()
    trend_list = forum_text.objects.all().order_by('-views')
    paginator1 = Paginator(trend_list, 5)
    page_number1 = request.GET.get('page1')
    trend = paginator1.get_page(page_number1)
    if request.method == 'POST':
        if request.POST.get('subject') and request.POST.get('query'):
            model=forum_text()
            model.user=request.user
            model.subject = request.POST.get('subject')
            model.query = request.POST.get('query')
            model.save()
            return HttpResponseRedirect(reverse('forum'))
        else:
            return render(request, 'index.html', {})
    else:
        return render(request, 'forum.html', {'model': mod,'pic': pic,'trend':trend})

# def forum_details(request):
def forum_details(request,forum_id):
    if request.user.is_authenticated:
        form = comment_box()
        mod = forum_text.objects.all()
        mod1 = forum_text.objects.get(id=forum_id)
        mod1.views = mod1.views+1
        mod1.save()
        pic = User.objects.all()
        num=deepcopy(forum_id)
        mode = Comment.objects.all()
        if request.method == 'POST':
            if request.POST.get('desc'):
                model = Comment()
                model.user = request.user
                temp=forum_text.objects.get(id=forum_id)
                model.forum = temp
                model.desc = request.POST.get('desc')
                model.save()
                return HttpResponseRedirect(reverse(forum_details, args=(forum_id,)))
            else:
                return render(request, 'index.html', {})
        else:
            return render(request, 'forum_details.html', {'forum_id': forum_id, 'form': form, 'model': mod, 'pic': pic,'mode':mode})
    else:
        return render(request,'login.html',{})

def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = forum_text.objects.get(id=post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        like,created = Like.objects.get_or_create(user=user,post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        like.save()
    return HttpResponseRedirect(reverse(forum_details,args=(post_id,)))

class HomePageView(TemplateView):
    template_name = 'forum.html'

class SearchResultsView(ListView):
    model = forum_text
    template_name = 'forumsearch.html'
    
    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = forum_text.objects.filter(
            Q(subject__icontains=query)
        )
        return object_list


@login_required
def special(request):
	return HttpResponse("You are logged in")

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

