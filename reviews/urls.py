from django.urls import path
from .views import *

app_name = "reviews"
urlpatterns = [
    path('write/', write, name="write"),  # 게시글 작성페이지
    path('ReviewList/', ReviewList, name="ReviewList"),  # 게시글 목룍 페이지
    path('SearchReview/', SearchReview, name="SearchReview"),  # 게시글 목룍 페이지
    path('<str:id>', ReviewDetail, name="ReviewDetail"),  # 게시글 자세히보는 페이지
    path('create/', create, name="create"),  # 게시글 작성함수
    # path('delete/',delete, name="delete"), #게시글 삭제함수
    path('<str:id>/create_comment', create_comment, name="create_comment"), #댓글 작성함수
    path('<int:review_id>/<int:comment_id>/delete_comment', delete_comment, name="delete_comment"),
    path('<int:review_id>/<int:comment_id>/update_comment', update_comment, name="update_comment"),

]
