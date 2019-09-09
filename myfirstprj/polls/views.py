from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from polls.models import Question
from django.urls.base import reverse
from django.http.response import HttpResponseRedirect

def index(request):
    latest_question_list = Question.objects.order_by(
        '-pub_date')
    return render(request, 'polls/index.html',
                  {"latest_question_list":latest_question_list})
 
def test(request):
    return render(request, 'polls/test.html')

def getform(request):
    return render(request, 'polls/getform.html')

def get(request):
    str1 = request.POST.get('str1')
    str2 = request.POST.get('str2')
    return render(request, 'polls/get.html',
                  {"str1":str1, "str2":str2})
    # str1이라는 이름의 str1자료를 보내주고 ""안에 있는게 넘기는거
    
def nameform(request):
    return render(request, 'polls/nameform.html')
    
def get_name(request):
    name = request.POST.get('name')
    return render(request, 'polls/get_name.html',
                  {"name":name})

def temp(request, temp):
    stemp = temp
    htemp = 1.8 * temp + 32 # htemp : 화씨, stemp : 섭씨
    return render(request, 'polls/ctof.html',
                  {"stemp":stemp, "htemp":htemp})
    # HttpResponse() 괄호안에는 str값만 들어감.
    
def bmi(request, height, weight):
    height = height / 100
    bmi = weight / (height * height)
    return render(request, 'polls/bmi.html',
                  {"height":height, "weight":weight, 
                   "bmi":round(bmi,3)})
    #round( , 3) 소수점 3자리까지 반올림!
    
def get_number(request, number):
    return HttpResponse('<h1>테스트 중입니다.' + 
                        str(number) + '</h1>')
    
def get_adult_result(request, age):
    return render(request, 'polls/adult_check.html',
                      {"age":age})
    
def get_two(request, num1, num2):
    return HttpResponse(str(num1) + " / " + str(num2))
    
def get_name_2(request, name):
    return HttpResponse("당신의 이름은? " + name)
    
def money(request, money1, money2):
    money1 = float(money1)
    money2 = float(money2)
    money2 = money2/170.20
    return HttpResponse("원화 : " + str(money1) + ", " +
                        "위안화 : " + str(round(money2, 3)))
    
def qtest(request):
    question_all = Question.objects.order_by('-pk')
    return render(request, 'polls/question_test.html',
           {"question_all":question_all})

def bus_price(request, price):
    return render(request, 'polls/price.html',
                  {"price":price})
    
def detail(request, id):
    # .get(조건)은 결과가 무조건 1개만 나올 때 쓸 수 있습니다.
    question = get_object_or_404(Question, pk=id)
    return render(request, 'polls/detail.html',
                  {'question':question})
    
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # 1~6개의 질문을 고르는 것
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # 그 질문에 해당되는 선택지를 고르는 것
    selected_choice.votes += 1
    selected_choice.save() # DB에 반영
    
    # polls의 results 패턴으로 이동하되 arg를 이용해 투표받은 항목의
    # 질문 번호를 같이 넘겨 주세요.
    return HttpResponseRedirect(
        reverse('polls:results', args = (question_id,)))
    
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html',
                  {'question':question})
    

    
    
    
    
    
    
    