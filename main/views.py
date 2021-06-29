from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone

def write(request):
    return render(request, 'write.html')

def ReviewList(request):
    blogs = Blog.objects.all()
    return render(request, 'ReviewList.html',{'blogs':blogs})

def ReviewDetail(request, id):
    blog = get_object_or_404(Blog, pk =id)
    return render(request, 'ReviewDetail.html',{'blog':blog})

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.pub_date = timezone.now()
    new_blog.body = request.POST['body']
    new_blog.save()
    return redirect('ReviewDetail', new_blog.id)
# Create your views here.
