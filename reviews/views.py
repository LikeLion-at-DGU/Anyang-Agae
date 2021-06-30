from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from django.utils import timezone

def write(request):
    return render(request, 'write.html')

def ReviewList(request):
    reviews = Review.objects.all()
    return render(request, 'ReviewList.html',{'reviews':reviews})

def create(request):
    new_reivew = Review()
    new_reivew.title = request.POST['title']
    new_reivew.pub_date = timezone.now()
    new_reivew.content = request.POST['content']
    new_reivew.save()
    return redirect('reviews:ReviewDetail', new_reivew.id)

def ReviewDetail(request, id):
    review = get_object_or_404(Review, pk =id)
    return render(request, 'ReviewDetail.html', {'review': review})
