from django.shortcuts import render
from reviews.models import Review

def main(request):
  review = Review.objects.all().order_by('-pub_date')
  reviews = review[:3]
  return render(request, 'main.html', {'reviews': reviews})