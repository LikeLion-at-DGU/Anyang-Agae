from django.shortcuts import render
from django.contrib.auth.models import User
from reviews.models import Review
from .models import Profile
# Create your views here.


def mypage(request):
    user = request.user
    reviews = Review.objects.filter(writer=user)
    profile = Profile.objects.filter(user=user)
    return render(request, 'users/mypage.html', {'reviews': reviews, 'profile': profile})
