from django.urls import path
from . import views

# app_name 변수는 주소에 라벨링을 합니다.
app_name="polls"

urlpatterns = [
        path('main', views.index, name='index'),
        path('test', views.test, name = 'test'),
        path('get', views.get, name ='get'),
        path('getform', views.getform, name = 'getform'),
        path('name', views.get_name, name = 'name'),
        path('nameform', views.nameform, name = 'nameform'),
        path('<int:temp>/ctof', views.temp),
        path('<int:height>/<int:weight>/bmi', views.bmi),
        path('<int:number>/content', views.get_number),
        # int가 들어왔을 때 number라는 변수에 저장
        # number라는 변수는 get_number라는 함수로 전달
        # 127.0.0.1:8000/polls/50
        #                         number
        path('<int:age>/check', views.get_adult_result),
        path('<int:num1>/<int:num2>/two', views.get_two),
        path('<str:name>/name', views.get_name_2),
        path('<str:money1>/<str:money2>/exchange', views.money),
        path('qtest', views.qtest),
        path('<int:price>/price', views.bus_price),
        path('<int:id>', views.detail, name='detail'),
        path('<int:question_id>/results/', views.results, name='results'),
        path('<int:question_id>/vote/', views.vote, name='vote'),
        
    ]
# http://www.127.0.0.1:8080/main