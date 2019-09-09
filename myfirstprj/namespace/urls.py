from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from namespace import views

app_name="namespace"

urlpatterns = [
    path('main', views.index, name="index"),
    path('lotto', views.lotto, name="lotto"),
    path('naver', views.naver, name="naver"),
    path('daum', views.daum, name="daum"),
    path('lottomove', views.lottomove, name="lottomove"),
]
# 위에서 아래로 왼쪽에서 오른쪽으로 스캔을 하기 때문에 polls/test에서 main페이지로
# 넘어갈 때 namespace의 main으로 이동함.