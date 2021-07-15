from django.shortcuts import render
from reviews.models import Review
from users.models import Profile


def main(request):
    review = Review.objects.all().order_by('-pub_date')
    reviews = review[:3]
    profile = Profile.objects.filter(is_opened='OPEN')
    return render(request, 'main.html', {'reviews': reviews, 'profile': profile})
