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

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length = 100)
    code = models.CharField(max_length = 5)
    budget = models.IntegerField(verbose_name = "Department Bedget")
    building = models.CharField(max_length = 10)

    def __str__(self):
        return self.name

class Semester(models.Model):
    code = models.IntegerField(verbose_name = "Semester Code")
    dept = models.ForeignKey(Department)
    credit = models.IntegerField()

    def __str__(self):
        return self.code

class Profile(models.Model):
    STUDENT = 'S'
    FACULTY = 'F'
    PROFILE_TYPES = (
        (STUDENT, 'Student'),
        (FACULTY, "Faculty Member")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length = 1, choices = PROFILE_TYPES)
    fathers_name = models.CharField(max_length = 100, verbose_name = "Father's Name")
    present_address = models.CharField(max_length = 200, default = "")
    permanent_address = models.CharField(max_length = 200, default = "")

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

class Student(Profile):
    addmission_year = models.PositiveIntegerField()
    current_sem = models.IntegerField(max_length=8)
    department = models.ForeignKey(Department)
    program = models.ForeignKey(Program)

    def get_courses(self):
        taken = CourseTaken.objects.filter(student = self, semester = self.current_sem)
        courses = []
        for course in taken:
            courses.append(course.course)
        return courses

    def comp(x, y):
        return x.username > y.username

class FaculyMember(Profile):
    department = models.ForeignKey(Department)

class Course(models.Model):
    name = models.CharField(max_length = 100)
    course_id = models.CharField(max_length = 20)
    provider_dept = models.ForeignKey(Department)

    def __str__(self):
        return self.name

class CourseTaken(models.Model):
    student = models.ForeignKey(Student)
    course = models.ForeignKey(Course)
    result = models.FloatField(verbose_name="Grade Point", default=0.0)
    year = models.IntegerField()
    semester = models.ForeignKey(Semester)
