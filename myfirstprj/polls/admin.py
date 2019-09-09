from django.contrib import admin

from .models import Question
from polls.models import Choice

admin.site.register(Question)
#admin에서 Question에 접근할 수 있는 권한 부여

admin.site.register(Choice)