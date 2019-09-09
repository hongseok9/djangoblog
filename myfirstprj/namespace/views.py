from django.shortcuts import render
import random
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse

def index(request):
    print(reverse('namespace:lotto'))
    print(reverse('polls:test'))
    print(reverse('polls:results', args=(10,)))
    return render(request, 'namespace/index.html')

def lotto(request):
    lottonum = []
    while len(lottonum) != 6:
        lotto = random.randint(1, 45)
        if lotto not in lottonum:
            lottonum.append(lotto)
    lottonum.sort()
    while lotto in lottonum:
        lotto = random.randint(1, 45)
    print(lottonum)
    print("2등 번호는 %d 입니다" % lotto)
    return render(request, 'namespace/lotto.html',
                  {'lottonum':lottonum,'lotto':lotto})
    
def naver(request):
    print("네이버 페이지로 강제 링크됩니다.")
    return HttpResponseRedirect('http://www.naver.com')

def daum(request):
    print("daum 사이트로 이동하셨습니다.")
    return HttpResponseRedirect('http://www.daum.net')

def lottomove(request):
    print("lotto 페이지로 이동하셨습니다.")
    return HttpResponseRedirect('lotto')

