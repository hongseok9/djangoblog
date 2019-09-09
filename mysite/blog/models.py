from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', 
                               on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    # 날짜, 시간, 글을 다 쓴 시간
    created_date = models.DateTimeField(
        default = timezone.now)
    # 꼭 기입 x 공개한 시간
    published_date = models.DateTimeField(
        blank=True, null=True)
    
    # 현재시간을 가져와서 DB에 반영
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return str(self.pk) + ". " + self.title + " " + str(self.created_date)[:10]
    
