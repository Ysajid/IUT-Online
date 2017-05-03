# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from models import Post, Group, Comment
from iut_online.calender.models import Event, EventManager
from iut_online.university.views import UniversityCalender
from datetime import datetime
from django.utils.safestring import mark_safe


@login_required
def post(request):
    if request.method == 'POST':
        # form = ArticleForm(request.POST)
        # if form.is_valid():
		post = Post()

		group = request.POST.get("group", None)
		user = request.user
		post.body = request.POST.get("body", "")
		post.user = request.user
		post.group = Group.objects.get(pk=group)
		post.type = request.POST.get("type", Post.GENERAL)
		post.save()

		if post.type != Post.GENERAL:
			e = Event()
			e.start_datetime = datetime.strptime(
			    request.POST.get("datetime", ""), '%m/%d/%Y %I:%M %p')
			e.end_datetime = e.start_datetime
			e.description = post.group.name + " quiz"
			e.save()

		return redirect('home')


@login_required
def comment(request):
	if request.method == "POST":
		comment = Comment()

		comment.user = request.user
		comment.post = Post.objects.get(pk=request.POST['post'])
		comment.text = request.POST['text']

		if(len(comment.text) > 0):
			comment.save()

		return redirect('home')


@login_required
def posts(request, group_pk):

	today = datetime.now()
	# events = EventManager.get_all_events(year = today.year, month = today.month, day = today.day)
	events = Event.objects.all()

	cal = UniversityCalender().formatmonth(today.year, today.month)
	print cal

	group = Group.objects.get(pk = group_pk)

	if(group.has_user(request.user)):
		groups = Group.get_groups()
		group_posts = Post.get_posts(group)
		return render(request, 'posts.html', {
			'types' : Post.TYPES,
			'all_posts' : group_posts,
			'current_group' : group,
			'groups' : groups,
			'calendar': "asd",
		})
	else :
		return None

def groups(request):
	groups = Group.get_groups()

	return render(request, 'manage.html', {
		'groups' : groups,
	})
