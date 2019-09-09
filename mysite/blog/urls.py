from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # 127.0.0.1:8000을 하면 바로 이 페이지가 나옴.
    # post/숫자 패턴으로 path를 만들어 주세요.
    # 함수 이름은 views.post_detail이며 name은 post_detail을 부여합니다.
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # 1버전대 문법
    # url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    # 위의 문법에서 url -> path로 대체되었음
    # r'^으로 시작하던 부분은 '로 대체되었음
    # (?P<pk>\d+)는 <int:pk>로 대체되었음
    # 패턴 마지막에 $를 붙이지 않아도 됨
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
]
