from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    # 질문 내용, charField : 문자 저장. 한글자 한글자 씩 저장, 최대 200글자
    pub_date = models.DateTimeField('date published')
    # 질문 한 날짜, date published : 나중에
    
    def __str__(self):
        return str(self.pk) + ". " + self.question_text + " " + str(self.pub_date)[:10]
    # __str__은 노출 되는 정보를 뭘로 만들건지를 정하는 것!
    # 여기서는 question_text를 노출 되게 만듬
    # 문자열로 출력
    
    
class Choice(models.Model): # 질문에 대한 항목
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE)
    # Question에 Choice를 넣어버리면 공간 낭비
    # Question은 하나씩만 저장하면 되지만 Choice는 여러개이므로 중복을 해야함.
    # 그러므로 Choice에서 FK를 사용하여 질문하나에 여러 답변을 사용
    choice_text = models.CharField(max_length=200)
    # 선택 항목
    votes = models.IntegerField(default=0)
    # 투표, 기본 속성으로 0 부여 
    
    def __str__(self):
        return str(self.question) + "|" + str(self.choice_text)
    
# PK는 자동으로 하나씩 들어감! 중복된 값 못가짐. 2번없어진다고 2번 안채워짐.