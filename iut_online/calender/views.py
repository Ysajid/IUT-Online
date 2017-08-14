from django.shortcuts import render
from datetime import datetime, date

from itertools import groupby
from calendar import HTMLCalendar
from django.utils.safestring import mark_safe
from models import EventManager, Event
from django.utils.html import conditional_escape as esc


# def calendar(request, year, month):
#   my_workouts = Workouts.objects.order_by('my_date').filter(
#     my_date__year=year, my_date__month=month
#   )
#   cal = WorkoutCalendar().formatmonth(year, month)
#   return render(request, 'calender/home.html', {'calendar': mark_safe(cal),})

def home(request):
    """
    Show calendar of events this month
    """
    today = datetime.now()
	# events = EventManager.get_all_events(year = today.year, month = today.month, day = today.day)
    events = Event.objects.all()
    cal = EventCalender(events).formatmonth(today.year, today.month)

    return render(request, 'calender/home.html', {'calendar': mark_safe(cal), })


class EventCalender(HTMLCalendar):

    def __init__(self, events=None):
        super(EventCalender, self).__init__()
        today = datetime.now()
        self.events = self.group_by_day(Event.objects.all())
        

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'

            if day in self.events:
                cssclass += ' filled'
                body = ['<br/>']
                for event in self.events[day]:
                    print "asd"
                    # body.append('<li>')
                    body.append('<a href="%s">' % "as")
                    body.append(esc(event.description))
                    body.append('</a><br/>')
                return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
            return self.day_cell(cssclass, day)
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(EventCalender, self).formatmonth(year, month)

    def group_by_day(self, events):
        if events != None:
            def field(event): return event.start_datetime.day
            return dict(
                [(day, list(items)) for day, items in groupby(events, field)]
            )

    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)
