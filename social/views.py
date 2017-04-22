from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import Context, loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from models import Post, Group
import time
from datetime import date

# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating
@login_required(login_url="login/")
def home(request):
	all_posts = Post.objects.all().order_by('posted_on').reverse()
	template = loader.get_template('home.html')
	
	return render(request, 'home.html' , {
		"all_posts" : all_posts
	})

def hello(request):
    text = "<h1>Hello World</h1>"
    return render(request , "hello.html", {})

def register_user(request):
	return render(request, 'register.html', {})

def logout(request):
	LogoutView.dispatch()
	return redirect('login')


@login_required
def post(request):
    if request.method == 'POST':
        # form = ArticleForm(request.POST)
        # if form.is_valid():
		post = Post()
		post.posted_on = date.fromtimestamp(time.time())

		group = Group.objects.all()[0]
		user = request.user
		post.text = request.POST.get("post", "")
		post.posted_by = user
		post.posted_in = group
		# article = Article()
		# article.create_user = request.user
		# article.title = form.cleaned_data.get('title')
		# article.content = form.cleaned_data.get('content')
		# status = form.cleaned_data.get('status')
		# if status in [Article.PUBLISHED, Article.DRAFT]:
		# article.status = form.cleaned_data.get('status')
		post.save()
		return redirect('home')

