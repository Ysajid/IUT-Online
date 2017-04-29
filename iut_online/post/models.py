# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length = 100)

    @staticmethod
    def get_groups(user=None):
        if user is None:
            return Group.objects.all()
        else:
            return Group.objects.filter(user = user)

    def get_users(self):
        users = []
        for rel in UsersInGroup.objects.filter(group = self):
            users.append(rel.user)
        return users

    def add_user(self, user):
        rel = UsersInGroup(group = self, user = user)
        rel.save()


class UsersInGroup (models.Model):
    group = models.ForeignKey(Group)
    user = models.ForeignKey(User)
    date_joined = models.DateField(auto_now_add=True)


class Post(models.Model):
    GENERAL = 'G'
    NOTICE = 'N'
    QUIZ = 'Q'
    ASSIGNMENT = 'A'
    TYPES = (
        (GENERAL, 'General'),
        (NOTICE, 'Notice'),
        (QUIZ, 'Quiz'),
        (ASSIGNMENT, 'Assignment')
    )
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default = None)
    type = models.CharField(max_length = 50, choices = TYPES, default = GENERAL)
    date = models.DateTimeField(auto_now_add=True, name = "post_date")
    body = models.TextField(max_length=255)
    like_cnt = models.IntegerField(default=0)
    comment_cnt = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ('-post_date',)

    def __str__(self):
        return self.body

    @staticmethod
    def get_posts(from_group=None):
        if from_group is not None:
            posts = Post.objects.filter(group=from_group)
        else:
            posts = Post.objects.filter()
        return posts

    # @staticmethod
    # def get_feeds_after(feed):
    #     feeds = Feed.objects.filter(parent=None, id__gt=feed)
    #     return feeds

    def get_comments(self):
        return Activity.objects.filter(activity_type=Activity.COMMENT,
                                        post=self.pk)

    def calculate_comments(self):
        self.comments = Feed.objects.filter(parent=self).count()
        self.save()
        return self.comments

    def get_likes(self):
        return Activity.objects.filter(activity_type=Activity.LIKE,
                                        post=self.pk)

    def calculate_likes(self):
        like_cnt = Activity.objects.filter(activity_type=Activity.LIKE,
                                        post=self.pk).count()
        self.like_cnt = like_cnt
        self.save()
        return self.like_cnt

    def get_likers(self):
        likes = self.get_likes()
        likers = []
        for like in likes:
            likers.append(like.user)
        return likers

    def comment(self, user, post):
        feed_comment = Post(user=user, post=post, parent=self)
        feed_comment.save()
        self.comments = Post.objects.filter(parent=self).count()
        self.save()
        return feed_comment


class Comment(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length = 100)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ('-date',)