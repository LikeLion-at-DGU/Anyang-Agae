from django.shortcuts import render, redirect, get_object_or_404, reverse
import datetime
from .models import Event
import calendar
from .calendar import Calendar
from django.utils.safestring import mark_safe
from .forms import EventForm
from django.contrib.auth.models import User


def calendar_view(request):
    today = get_date(request.GET.get('month'))

    user = request.user
    prev_month_var = prev_month(today)
    next_month_var = next_month(today)

    cal = Calendar(today.year, today.month, user)
    html_cal = cal.formatmonth(withyear=True)
    result_cal = mark_safe(html_cal)

    context = {'calendar': result_cal, 'prev_month': prev_month_var,
               'next_month': next_month_var, }

    return render(request, 'diary/events.html', context)

# 현재 달력을 보고 있는 시점의 시간을 반환


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime.date(year, month, day=1)
    return datetime.datetime.today()

# 현재 달력의 이전 달 URL 반환


def prev_month(day):
    first = day.replace(day=1)
    prev_month = first - datetime.timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

# 현재 달력의 다음 달 URL 반환


def next_month(day):
    days_in_month = calendar.monthrange(day.year, day.month)[1]
    last = day.replace(day=days_in_month)
    next_month = last + datetime.timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

# 새로운 Event의 등록 혹은 수정

# Create your views here.

# 일정 등록


def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.writer = request.user
            event.save()
            return redirect('diary:calendar')
    else:
        form = EventForm()
    context = {'form': form}
    return render(request, 'diary/input.html', context)


def event_edit(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.writer = request.user
            event.save()
            return redirect('diary:detail', event_id=event.id)
    else:
        form = EventForm(instance=event)
    context = {'form': form}
    return render(request, 'diary/input.html', context)


def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'diary/diarydetail.html', {'event': event})


def delete(request, event_id):
    event = Event.objects.get(id=event_id)
    event.delete()
    return redirect('diary:calendar')
