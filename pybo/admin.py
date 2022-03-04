

# Register your models here.
from django.contrib import admin
from .models import Question

# admin.site.register(Question)
# 퀘스쳔 모델을 임포트했다. 이제 어드민화면에서 퀘스쳔 모델을 관리할 수 있다. 생성 조회 수정 삭제 가능.

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)