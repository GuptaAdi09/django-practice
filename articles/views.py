from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Articles
import random 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def article_with_HTTpResponse(request):
        # FIRST WAY TO RETRIVE THE DATA
        # random_id = randint(1,3)
        # response_content = f'<div style="background-color: green; padding: 20px; margin-top: 25px;">{Articles.objects.get(id=random_id).name}</div>' 
        # return HttpResponse(response_content)
        
    #SECOND WAY TO RETRIVE THE DATA
    all_articles = Articles.objects.all() # this query pull all obj
    print(Articles.objects.get(id=1)) # this query pull obj which had id 1 , 

    response_content = ""
    for article in all_articles:
        # print(article.id)
        
        if article.id == 1:
            
            response_content += f'<div style="background-color: green; padding: 20px; margin-top: 25px;">' \
                            f'U are inside the article app, and u are hitting this request for this article => ' \
                            f'<h4 style="color:darkblue;">{article.id}. {article.name} by {article.author}</h4></div><br>'
            
        response_content += f'<div style="background-color: lightblue; padding: 20px; margin-top: 25px;">' \
                            f'U are inside the article app, and u are hitting this request for this article => ' \
                            f'<h4 style="color:darkblue;">{article.id}. {article.name} by {article.author}</h4></div><br>'
    return HttpResponse(response_content)


def article_with_htmlResponse(request):
    # print("HTML function is call")
    # picking random articles
    obj = Articles.objects.all()
    
    return render(request, 'htmlResponse_article.html', context={"all_article":obj})


def description_view(request,*args, **kwargs):
    
    get_object_or_404(Articles,pk=kwargs['id'])
    get_obj = Articles.objects.get(id=kwargs['id'])
    
    return HttpResponse(f"<h1>{get_obj.discription}</h1>")

def search_article(request):
    # print(dir(request))
    query = request.GET.get('query')
    print(query)
    
    try:
        obj = Articles.objects.get(id=int(query))
        return render(request,'search_article.html',context={
            "id":obj.id,
            "name": obj.name,
            "author": obj.author,
            "discription": obj.discription

        })
    except:
        context = {
            "error": "ARTICLE DOES NOT EXITS"
        }
        return render(request,'search_article.html',context)


@login_required
def create_articel(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            article_obj = Articles.objects.create(
               name = request.POST['name'],
               author = request.POST['author'],
               discription = request.POST['discription'])
            return redirect(f'/htmlResponseArticle/create/?article_id={article_obj.id}')
        article_obj = None
        if 'article_id' in request.GET:
            article_obj = Articles.objects.filter(id=request.GET['article_id']).first()
        
        context = {'article_obj':article_obj,'is_created':bool(article_obj)}
        return render(request,'create.html',context)
    else:
        return redirect('login_user')



def login_user(request):

    if request.method == 'POST':
        UserName = request.POST.get('user_name')
        Pass = request.POST.get('password')
        try:
            user = User.objects.get(username=UserName)
        except User.DoesNotExist:
            return redirect('register_user')
        if user:
            user = authenticate(username=UserName,password=Pass)
            if user is not None:
                login(request,user)
                return redirect('create_articel')
            
        return render(request,"login_user.html",{"error": "Invalid username or password"})
    return render(request,"login_user.html",{})

def search_item(request):
    if request.method == "GET":
        query = request.GET.get("query","")
        if query:
            results = Articles.objects.filter(name__icontains=query)
            data = [{
                "id": item.id,
                "name": item.name,
                "discription": item.discription
            } for item in results]
            return JsonResponse({"success":True,"results":data})
    return JsonResponse({"success":False, "result":[] })

def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_user')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'register.html',{'form':form})


def logout_user(request):
    logout(request)
    return redirect('login_user')