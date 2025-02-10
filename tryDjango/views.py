'''
    views are used to render the html page 
'''
from django.http import HttpResponse
from django.shortcuts import render

def home(request,*args, **kwargs):
    print(f"the arg is {args} and kwaegs is {kwargs}")
    name = "aditya"
    context = {
        'name':name,
        "request":request
    }
    
    
    
    """ take in a request and return HTML as a response"""
    return render(request,'home.html',context)
    # print("function call")
    # return HttpResponse("<h1>Hello world</h1>")