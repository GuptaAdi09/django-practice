from django.urls import path

from .views import index,detail,result,vote

app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('',index,name='index'),
    # /polls/2/
    path("<int:question_id>/",detail,name="detail"),
    # /polls/2/result/
    path("<int:question_id>/result/",result,name="result"),
    # /polls/2/vote/
    path("<int:question_id>/vote/",vote,name="vote"),
    




]