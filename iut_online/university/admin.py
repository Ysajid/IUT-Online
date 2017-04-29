# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Semester)
admin.site.register(FaculyMember)
admin.site.register(CourseTaken)