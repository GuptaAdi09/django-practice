from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.db.models import F
from django.urls import reverse


from .models import Question,choice




def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    return render(request,'polls/index.html',context={'latest_question_list':latest_question_list})


def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',context={'question':question})

def result(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    
    return render(request,'polls/results.html',{"question":question})

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
        
    except (KeyError, choice.DoesNotExist):
        # HttpResponse("Something wrong")
        return render(request,"polls/detail.html",{
            "question": question,
            "error_message": "You did not select a choice",
        })
    else:
        print(f"Before update: {selected_choice.votes}")  # Debugging
        choice.objects.filter(pk=selected_choice.pk).update(votes=F("votes") + 1)
        selected_choice.refresh_from_db()
        print(f"After update: {selected_choice.votes}")


    return HttpResponseRedirect(reverse('polls:result',args=(question.id,)))

