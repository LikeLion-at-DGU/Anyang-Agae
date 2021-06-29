from django.urls import path
from .views import *

app_name="main"
urlpatterns = [
    path('write/', write, name="write"), #게시글 작성페이지
    path('ReviewList/',ReviewList, name="ReviewList"), #게시글 목룍 페이지   
    path('<str:id>',ReviewDetail, name="ReviewDetail"), #게시글 자세히보는 페이지
    path('create/',create, name="create"), #게시글 작성함수
]