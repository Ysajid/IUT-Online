# from forms import RegistrationForm
import time
from datetime import date, datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import Context, loader

from iut_online.post.models import Group, Post
from iut_online.calender.models import Event, EventManager
from iut_online.calender.views import EventCalender
from models import Department, Profile, Program, Student
import exceptions
from django.utils.safestring import mark_safe


# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating
@login_required(login_url="login/")
def home(request):
	all_posts = Post.objects.all()
	groups = Group.get_groups(request.user)

	today = datetime.now()
	events = EventManager.get_all_events(
		year = today.year, month = today.month, day = today.day)
		
		
	cal = UniversityCalender().formatmonth(today.year, today.month)
	print cal
	
	return render(request, 'home.html' , {
		'types' : Post.TYPES,
		'all_posts' : all_posts,
		'groups' : groups,
		'calendar': mark_safe(cal),
	})

def hello(request):
    resp = HttpResponse( stream_response_generator())
    return resp

def stream_response_generator():
    yield "<html><body>\n"
    for x in range(1,11):
        yield "<div>%s</div>\n" % x
        # yield " " * 1024  # Encourage browser to render incrementally
        # time.sleep(1)	
    yield "</body></html>\n"

def register_user(request):
	if request.method == 'POST':

		addmission_year = request.POST.get("addmission_year")
		department = Department.objects.get(pk = request.POST.get("department"))
		program = Program.objects.get(pk = request.POST.get("program"))

		students = Student.objects.filter(addmission_year = addmission_year, department = department, program = program)

		if(students.count() != 0):
			username = str(int(max(students, key = lambda x: x.user.username).user.username) + 1)
		else :
			username = addmission_year[2:] + str(department.pk) + str(program.year) + "01"

		# username = request.POST.get("addmission_year")[2:] + request.POST.get("department") + str(Program.objects.get(pk = request.POST.get("program")).year) + str(Student.objects.filter(addmission_year = request.POST.get("addmission_year")).count() + 1)
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
		student.department = department
		student.program = program
		student.save()

		# user = authenticate(username=user, password=user.password, email = email)
		# login(request, user)

		return redirect('home')


	depts = Department.objects.all()
	progs = Program.objects.all()
	# form = RegistrationForm()
	return render(request, 'register.html', {
		"depts" : depts,
		"progs" : progs,
		# 'form' : form
	})


class UniversityCalender(EventCalender):

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'

            if day in self.events:
                cssclass += ' filled'
                body = [' ']
                for event in self.events[day]:
                    print "asd"
                    # body.append('<li>')
                    # body.append('<a href="%s">' % "as")
                    # body.append(esc(event.description))
                    body.append('<span class="glyphicon glyphicon-bell" style="color:coral;" ></span>')
                return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
            return self.day_cell(cssclass, day)
        return self.day_cell('noday', '&nbsp;')


def logout(request):
	LogoutView.dispatch()
	return redirect('login')
