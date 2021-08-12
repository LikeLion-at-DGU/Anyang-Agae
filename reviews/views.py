from django.shortcuts import render, redirect, get_object_or_404
from .models import Review, Comment
from django.db.models import Q, Count
from django.utils import timezone
from django.core.paginator import Paginator


def write(request):
    return render(request, 'reviews/write.html')


def SearchReview(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/SearchReview.html', {'reviews': reviews})


def ReviewList(request):
    reviews = Review.objects.all().order_by('-pub_date')
    # # 정렬
    # so = request.GET.get('so','recent')
    # if so == 'recommend': # 추천 순
    #     reviews = Review.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-pub_date')
    # elif so == 'click': # 클릭 순
    #     reviews = Review.objects.annotate(num_view=Count('view_count')).order_by('-num_view', '-pub_date')
    # elif so == 'review': # 리뷰 순
    #     reviews = Review.objects.annotate(num_review=Count('comments')).order_by('-num_review', '-pub_date')
    # else: # 최신 순
    #     reviews = Review.objects.order_by('-pub_date')

    # 검색
    kw = request.GET.get('kw', '')  # 검색어
    if kw:
        reviews = reviews.filter(  # reviews로 받고 아래에서 page당 3개씩 받는 원리
            Q(title__icontains=kw) |  # 제목검색
            Q(writer__username__icontains=kw)  # writer검색
        ).distinct()

    # pagination
    paginator = Paginator(reviews, 3)
    page = request.GET.get('page', '1')  # 페이지
    page_obj = paginator.get_page(page)

    context = {'reviews':page_obj, 'kw' : kw, 'page':page}
    return render(request, 'reviews/ReviewList.html', context)


def create(request):
    new_reivew = Review()
    new_reivew.title = request.POST['title']
    new_reivew.pub_date = timezone.now()
    new_reivew.hospital = request.POST['hospital']
    new_reivew.content = request.POST['content']
    new_reivew.writer = request.user
    new_reivew.save()
    return redirect('reviews:ReviewDetail', new_reivew.id)


def ReviewDetail(request, id):
    review = get_object_or_404(Review, pk=id)
    review.view_count += 1
    review.save()
    all_comments = review.comments.all().order_by('-created_at')
    return render(request, 'reviews/ReviewDetail.html', {'review': review, 'comments': all_comments})


def create_comment(request, id):
    if request.method == "POST":
        review = get_object_or_404(Review, pk=id)
        current_user = request.user
        content = request.POST.get('content')
        Comment.objects.create(content=content, writer=current_user, review=review)
    return redirect('reviews:ReviewDetail', id)

def update_comment(request, review_id, comment_id):
    review = get_object_or_404(Review, pk=review_id)
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method=="POST":
        comment.content = request.POST['content']
        comment.save()
        # all_comments = review.comments.all()
        return redirect('reviews:ReviewDetail', review.pk)
    return render(request, 'reviews/update_comment.html', {'comment' :comment})

def delete_comment(request, review_id, comment_id):
    review = get_object_or_404(Review, pk=review_id)
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('reviews:ReviewDetail', review.pk)
