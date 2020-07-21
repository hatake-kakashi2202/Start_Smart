from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.utils import timezone
from .models import blog
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import TemplateView, ListView

# Create your views here.
def allblogs(request):
	if not request.user.is_authenticated:
		return render(request, 'login.html')
	all_blogs = blog.objects
	all_blogs_temp = blog.objects.all()
	l = []
	for x in all_blogs_temp:
		if len(x.inter)>20:
			x.inter = x.inter[3:]
			temp = x.inter.split(' ')
			count = 0
			for x in temp:
				if len(x) > 2:
					count = count+1
			l.append(temp[0] + ' and ' + str(count-1) + ' more')
		else:
			l.append(x.inter)
	all_blogs_temp = list(zip(all_blogs_temp, l))
	page = request.GET.get('page', 1)
	paginator = Paginator(all_blogs_temp, 10)
	try:
		users = paginator.page(page)
	except PageNotAnInteger:
		users = paginator.page(1)
	except EmptyPage:
		users = paginator.page(paginator.num_pages)
	return render(request, 'allblogs.html', {'all_blogs':users})

def create(request):
	if not request.user.is_authenticated:
		return render(request, 'login.html')
	if request.method == 'POST':
		if request.POST['title'] and request.POST['body']:
			new_blog = blog()
			new_blog.title = request.POST['title']
			new_blog.body = request.POST['body']
			new_blog.writer = request.user
			new_blog.pub_date = timezone.datetime.now()
			new_blog.save()
			# return redirect('/blogs/'+str(new_blog.id))
			return redirect('allblogs')
		else:
			return render(request, 'create.html', {'error':'all fields required'})
	else:
		return render(request, 'create.html')


def detail(request, blog_id):
	curr_blog = get_object_or_404(blog, pk = blog_id)
	return render(request, 'detail.html', {'curr_blog':curr_blog})

def myblogs(request):
	blog_list = []
	data = serializers.serialize('python', blog.objects.all(), fields=('pk'))
	for z in data:
		curr_blog = blog.objects.get(pk = z['pk'])
		if curr_blog.writer == request.user:
			blog_list.append(curr_blog)
	return render(request, 'myblogs.html', {'blog_list':blog_list})



def interest(request, blog_id):
	

	curr_blog = get_object_or_404(blog, pk = blog_id)

	if request.user.username not in curr_blog.inter:
		curr_blog.inter = curr_blog.inter + "  "+ request.user.username
		curr_blog.save()
	
	return redirect('allblogs')
	

def likers(request, blog_id):
	curr_blog = get_object_or_404(blog, pk = blog_id)
	interest = curr_blog.inter
	like = []
	check = []
	names = interest.split()
	for abc in names:
		user = User.objects.get(username = abc)
		try:
			if user.startup is not None:
				is_startup = True
		except:
			is_startup = False
		check.append(is_startup)
		like.append(user)
	like = zip(like, check)

	return render(request, 'likers.html', {'like':like})

# @login_required
def delete_blog(request, blog_id):
	if not request.user.is_authenticated:
		return render(request, 'login.html')
	curr_blog = blog.objects.get(pk = blog_id)
	curr_blog.delete()
	# return myblogs(request)
	return redirect('allblogs')

# def listing(request):
# 	blog_list = blog.objects.all()
# 	paginator = Paginator(blog_list, 2)


# 	page_number = request.GET.get('page')
# 	page_obj = paginator.get_page(page_number)
# 	page_obj1 = dict.fromkeys(page_obj, 0) 

# 	obj_list = []
# 	for i in page_obj1:
# 		user = blog.objects.get(pk = i.id)
# 		obj_list.append(user)
# 	print(type(obj_list))
# 	obj_tup = tuple(obj_list)
# 	print(type(obj_tup))
# 	return render(request, 'listing.html', {'page_obj', obj_tup})

class HomePageView(TemplateView):
    template_name = 'allblogs.html'

class SearchResultsView(ListView):
    model = blog
    template_name = 'blogsearch.html'
    
    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = blog.objects.filter(
            Q(title__icontains=query)
        )
        return object_list