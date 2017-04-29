from django.db import models
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.models import User
from django import forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))

class Program(models.Model):
    name = models.CharField(max_length = 100)
    code = models.CharField(max_length = 10)
    year = models.IntegerField()

class Department(models.Model):
    name = models.CharField(max_length = 100)
    code = models.CharField(max_length = 5)
    budget = models.IntegerField(verbose_name = "Department Bedget")
    building = models.CharField(max_length = 10)

class Semester(models.Model):
    code = models.IntegerField(verbose_name = "Semester Code")
    dept = models.ForeignKey(Department)
    credit = models.IntegerField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fathers_name = models.CharField(max_length = 100, verbose_name = "Father's Name")
    present_address = models.CharField(max_length = 200, default = "")
    permanent_address = models.CharField(max_length = 200, default = "")

class Student(Profile):
    addmission_year = models.PositiveIntegerField()
    current_sem = models.IntegerField(max_length=8)
    department = models.ForeignKey(Department)

    def get_courses(self):
        taken = CourseTaken.objects.filter(student = self, semester = self.current_sem)
        courses = []
        for course in taken:
            courses.append(course.course)
        return courses

class FaculyMember(Profile):
    department = models.ForeignKey(Department)

class Course(models.Model):
    name = models.CharField(max_length = 100)
    course_id = models.CharField(max_length = 20)
    provider_dept = models.ForeignKey(Department)

class CourseTaken(models.Model):
    student = models.ForeignKey(Student)
    course = models.ForeignKey(Course)
    result = models.FloatField(verbose_name="Grade Point", default=0.0)
    year = models.IntegerField()
    semester = models.ForeignKey(Semester)
