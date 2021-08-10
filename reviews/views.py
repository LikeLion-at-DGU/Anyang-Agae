from django.shortcuts import render, redirect, get_object_or_404
from .models import Review, Comment
from django.db.models import Q
from django.utils import timezone
from django.core.paginator import Paginator

def write(request):
    return render(request, 'reviews/write.html')

def SearchReview(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/SearchReview.html',{'reviews':reviews})

def ReviewList(request):
    reviews = Review.objects.all()
    # pagination
    paginator = Paginator(reviews, 3)
    page = request.GET.get('page', '1')  # 페이지
    page_obj = paginator.get_page(page)

    # 검색
    kw = request.GET.get('kw', '')  # 검색어
    if kw:
        reviews = reviews.filter(
            Q(title__icontains=kw) | # 제목검색
            Q(writer__username__icontains=kw) # writer색
        ).distinct()

    context = {'reviews':reviews, 'kw' : kw, 'page_obj' : page_obj}
    # 'page_obj' : page_obj, 'page' : page
    return render(request, 'reviews/ReviewList.html', context)

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
    all_comments = review.comments.all().order_by('-created_at')
    return render(request, 'reviews/ReviewDetail.html', {'review': review, 'comments':all_comments})

def create_comment(request, id):
    if request.method == "POST":
        review = get_object_or_404(Review, pk=id)
        current_user = request.user
        content = request.POST.get('content')
        Comment.objects.create(content=content, writer=current_user, review=review)
    return redirect('reviews:ReviewDetail', id)