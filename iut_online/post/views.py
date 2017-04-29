# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from models import Post, Group


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
		post.group = Group.objects.get(pk = group)
		# article = Article()
		# article.create_user = request.user
		# article.title = form.cleaned_data.get('title')
		# article.content = form.cleaned_data.get('content')
		# status = form.cleaned_data.get('status')
		# if status in [Article.PUBLISHED, Article.DRAFT]:
		# article.status = form.cleaned_data.get('status')
		post.save()
		return redirect('home')
	
@login_required
def posts(request, group_pk):
	
	group = Group.objects.get(pk = group_pk)
	groups = Group.get_groups()
	group_posts = Post.get_posts(group)
	return render(request, 'home.html', {
		'all_posts' : group_posts,
		'current_group' : group,
		'groups' : groups,
	})

