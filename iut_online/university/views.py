# from forms import RegistrationForm
import time
from datetime import date

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import Context, loader

from iut_online.post.models import Group, Post
from models import Department, Profile, Program, Student
import exceptions


# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating
@login_required(login_url="login/")
def home(request):
	all_posts = Post.objects.all()
	groups = Group.get_groups()
	
	return render(request, 'home.html' , {
		'all_posts' : all_posts,
		'groups' : groups,
	})

def hello(request):
    text = "<h1>Hello World</h1>"
    return render(request , "hello.html", {})

def register_user(request):
	if request.method == 'POST':

		addmission_year = request.POST.get("addmission_year")
		department = Department.objects.get(pk = request.POST.get("department"))
		program = Program.objects.get(pk = request.POST.get("program"))

		students = Student.objects.filter(addmission_year = addmission_year, department = department, program = program)

		if(students.count() != 0):
			username = 

		if()
		username = request.POST.get("addmission_year")[2:] + request.POST.get("department") + str(Program.objects.get(pk = request.POST.get("program")).year) + str(Student.objects.filter(addmission_year = request.POST.get("addmission_year")).count() + 1)
		first_name = request.POST.get("first_name")
		last_name = request.POST.get("last_name")

		email = first_name + last_name + username + "@iut-dhaka.edu"
		email = email.lower()

		user, created = User.objects.get_or_create(username=username, email=email)

		user.set_password(request.POST.get("password"))

		user.first_name = first_name
		user.last_name = last_name

		user.save()

		try:
			student = Student.objects.get(user = user)
		except Exception as identifier:
			student = Student()
			
		student.user = user
		student.fathers_name = request.POST.get("father's_name")
		student.present_address = request.POST.get("present_address")
		student.permanent_address = request.POST.get("permanent_address")
		student.addmission_year = request.POST.get("addmission_year")
		student.current_sem = int(request.POST.get("current_sem", "1"))
		student.department = Department.objects.get(pk = request.POST.get("department"))
		student.save()

		user = authenticate(username=user, password=user.password)
		login(request, user)

		return redirect('home')


	depts = Department.objects.all()
	progs = Program.objects.all()
	# form = RegistrationForm()
	return render(request, 'register.html', {
		"depts" : depts,
		"progs" : progs,
		# 'form' : form
	})



def logout(request):
	LogoutView.dispatch()
	return redirect('login')
