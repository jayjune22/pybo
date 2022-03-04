from django.urls import path

from . import views

app_name = 'pybo'

# urlpatterns = [
#     path('', views.index),
# ]
#기존 config/urls.py 파일에 설정했던 내용과 별반 차이가 없다.
# 다만 path('', views.index) 처럼 pybo/ 가 생략된 '' 이 사용되었다.
# 이렇게 되는 이유는 config/urls.py 파일에서 이미 pybo/로 시작하는 URL이 pybo/urls.py 파일과 먼저 매핑되었기 때문이다.

urlpatterns = [
    # path('', views.index),
    path('', views.index, name='index'),
    # path('<int:question_id>/', views.detail),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]

#path('<int:question_id>/', views.detail) 라는 URL 매핑을 추가하였다.
# 이제 http://localhost:8000/pybo/2/ 페이지가 요청되면 위 매핑 룰에 의해
# http://localhost:8000/pybo/<int:question_id>/ 가 적용되어 question_id 에
# 2가 저장되고 views.detail 함수가 실행될 것이다. <int:question_id> 에서 int는 숫자가 매핑됨을 의미한다.