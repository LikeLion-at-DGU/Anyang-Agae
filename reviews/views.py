from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from django.db.models import Q
from django.utils import timezone

def write(request):
    return render(request, 'reviews/write.html')

def SearchReview(request):
    kw = request.GET.get('kw', '')  # 검색어
    reviews = Review.objects.all()
    # 검색
    if kw:
        reviews = reviews.filter(
            Q(title__icontains=kw) # 제목검색
        ).distinct()
    return render(request, 'reviews/SearchReview.html',{'reviews':reviews, 'kw' : kw})

def ReviewList(request):
    reviews = Review.objects.all()
    kw = request.GET.get('kw', '')  # 검색어
    # 검색
    if kw:
        reviews = reviews.filter(
            Q(title__icontains=kw) # 제목검색
        ).distinct()
    return render(request, 'reviews/ReviewList.html',{'reviews':reviews, 'kw' : kw})

def create(request):
    new_reivew = Review()
    new_reivew.title = request.POST['title']
    new_reivew.pub_date = timezone.now()
    new_reivew.content = request.POST['content']
    new_reivew.writer=request.user
    new_reivew.save()
    return redirect('reviews:ReviewDetail', new_reivew.id)

def ReviewDetail(request, id):
    review = get_object_or_404(Review, pk =id)
    return render(request, 'reviews/ReviewDetail.html', {'review': review})
