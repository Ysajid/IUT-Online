from __future__ import unicode_literals

from datetime import date, datetime
from django.db import models
from datetime import datetime


# @python_2_unicode_compatible
class RepeatRules(models.Model):
    
    YEARLY = 'Y'
    BIYEARLY = "y"
    MONTHLY = "M"
    WEEKLY = "W"
    BIWEEKLY = "w"
    DAILY = "D"
    REPEAT_OPTIONS = (
        (YEARLY, "Yearly"),
        (BIYEARLY, "Biyearly"),
        (MONTHLY, "Monthly"),
        (WEEKLY, "Weekly"),
        (BIWEEKLY, "Biweekly"),
        (DAILY, "Daily")
    )

# @python_2_unicode_compatible
class Event(models.Model):
    start_datetime = models.DateTimeField(verbose_name="Event starts at")
    end_datetime = models.DateTimeField(verbose_name="Event ends at")
    repeat = models.CharField(max_length=1, choices=RepeatRules.REPEAT_OPTIONS, null=True)
    description = models.CharField(max_length = 200, verbose_name="Description")
    final_endtime = models.DateTimeField(null=True, blank=True)
    place = models.CharField(max_length=100, null=True)


class EventManager():

    @staticmethod
    def get_all_events():
        return Event.objects.all()

    @staticmethod
    def get_all_events(year):
        
        all_events = Event.objects.all()
        selected_events = []
        for event in all_events:
            if event.start_datetime.year == year:
                selected_events.append(event)
        
        return selected_events

    @staticmethod
    def get_all_events(year, month):

        all_events = Event.objects.all()
        selected_events = []
        for event in all_events:
            if event.start_datetime.month == month and event.start_datetime.year == year:
                selected_events.append(event)
        return selected_events

    @staticmethod
    def get_all_events(year,month,week):

        all_events = Event.objects.all()
        selected_events = []
        for event in all_events:
            if event.start_datetime == week and event.start_datetime.month == month and event.start_datetime.year == year:
                selected_events.append(event)
        return selected_events
         
    @staticmethod   
    def get_all_events(year, month, day):
        all_events = Event.objects.all()
        selected_events = []
        for event in all_events:
            if event.start_datetime == day and event.start_datetime.month == month and event.start_datetime.year == year:
                selected_events.append(event)
                
        return selected_events


    @staticmethod
    def get_events_between(startdate, enddate):
        events = Event.objects.filter(start_datetime__gte = startdate, end_datetime__lte = enddate)
        return events
            