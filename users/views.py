from django.shortcuts import render
from django.contrib.auth.models import User
from reviews.models import Review
from .models import Profile
from diary.models import Event
# Create your views here.


def mypage(request):
    user = request.user
    reviews = Review.objects.filter(writer=user)
    profile = Profile.objects.filter(user=user)
    events = Event.objects.filter(writer=user)
    context = {
        'reviews': reviews,
        'profile': profile,
        'events': events,
    }
    return render(request, 'users/mypage.html', context)
