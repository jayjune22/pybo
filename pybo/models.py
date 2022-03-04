from django.db import models

# Create your models here.
from django.db import models


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject
    #모델에 메서드가 추가될 경우에는 makemigrations와 migrate를 수행할 필요가 없다.
    # migrate 명령이 필요한 경우는 모델의 속성이 변경되었을때 뿐이다.

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

