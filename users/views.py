from django.shortcuts import render
from django.contrib.auth.models import User
from reviews.models import Review
# Create your views here.

def mypage(request):
    user = request.user
    reviews = Review.objects.filter(writer=user)
    return render(request, 'users/mypage.html',{'reviews':reviews})